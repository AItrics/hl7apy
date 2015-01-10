# -*- coding: utf-8 -*-
#
# Copyright (c) 2012-2014, CRS4
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import sys
import os
import re
from optparse import OptionParser
from lxml import objectify
import pprint
import collections
import cPickle

class ProfileParser(object):

    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.parse_profiles()

    def _sanitize(self, s):
        if s is not None:
            s = s.strip().upper()
            s = re.sub("\W+", "_", s)
            if s.endswith('_'):
                s = s[:-1]
            if s.startswith('_'):
                s = s[1:]
            m = re.match("^(C[MNKQ])(_[A-Z]+\d*){1,}(_\d+){0,}$", s)
            if m is not None:
                s = re.sub("_\d+$", "", s)
                s = s[2:].replace("_", "")
                s += m.groups()[2] or ''
        return s

    def _get_cardinality(self, obj):
        min = obj.get('Min') if obj.get('Min') is not None else 0
        max = obj.get('Max') if obj.get('Max') is not None else -1
        if max == "*":
            max = -1
        if obj.get('Usage') == "X":
            min = max = 0
        elif obj.get('Usage') == "R":
            min = 1
        min = int(min)
        max = int(max)

        return min, max

    def _parse_children(self, parent, parent_name):
        children = []
        for child in parent.getchildren():
            child_name = child.get('Name')
            cardinality = self._get_cardinality(child)
            if child.tag == 'Segment':
                segment_children = self._parse_segment(child)
                children.append(('cp', 'sequence', segment_children, child_name, cardinality, 'Segment'))
            elif child.tag == 'SegGroup':
                group_name = "{}_{}".format(parent_name, child_name)
                group_children = self._parse_children(child, parent_name)
                children.append(('cp', 'sequence', group_children, group_name, cardinality, 'Group'))
        return tuple(children)

    def _parse_segment(self, segment):
        name = segment.get('Name')
        fields = []
        for index, field in enumerate(segment.Field):
            field_name = "{}_{}".format(name, index+1)
            field_datatype =  field.get('Datatype')
            field_cardinality = self._get_cardinality(field)
            field_length = int(field.get('Length')) if field.get('Length') else 0
            field_table = "HL7{}".format(field.get('Table')) if field.get('Table') else None
            field_children = self._parse_datatype(field)
            field_type = 'sequence' if len(field_children) > 1 else 'leaf'
            field_data = ['cp', field_type, field_children, field_name, field_cardinality, 'Field',
                          field_datatype.upper(), field_length, field_table]
            # field_data = [field_name, field_cardinality, self._parse_field(field), 'Field']
            fields.append(tuple(field_data))

        return tuple(fields)

    def _parse_datatype(self, parent):
        components = []
        # length = int(field.get('Length')) if field.get('Length') else 0
        # table = "HL7{}".format(field.get('Table')) if field.get('Table') else None
        datatype =  parent.get('Datatype')
        for type in ['Component', 'SubComponent']:
            try:
                for c_index, component in enumerate(getattr(parent, type)):
                    comp_name = "{}_{}".format(datatype, c_index+1)
                    comp_cardinality = (1,1) if component.get('Usage') in ('R',) else (0, 1)
                    comp_datatype = component.get('Datatype')
                    comp_length = int(component.get('Length')) if component.get('Length') else 0
                    comp_table = "HL7{}".format(component.get('Table')) if component.get('Table') else None
                    comp_children = self._parse_datatype(component)
                    comp_type = 'sequence' if len(comp_children) > 1 else 'leaf'
                    component_data = ('cp', comp_type, comp_children, comp_name, comp_cardinality,
                                      type, comp_datatype.upper(), comp_length, comp_table)
                    # component_data = (comp_name, cardinality, self._parse_field(component), type)
                    components.append(component_data)
            except:
                continue

        return tuple(components)

    def parse_profiles(self):
        files = [f for f in os.listdir(self.input_path) if f.endswith('.xml')]
        try:
            if not os.path.exists(self.output_path):
                os.mkdir(self.output_path)
        except Exception, ex:
            print "Error occurred while saving the output to: ", self.output_path, ex
            sys.exit(1)

        for f in files:
            filename, ext = os.path.splitext(f)
            content = self.parse_profile(f)
            file_path = os.path.join(self.output_path, filename)
            print content
            with open(file_path, "wb") as output_file:
                cPickle.dump(dict(content), output_file)

    def parse_profile(self, file):
        """
        Parses the given message profile file using the lxml library then returns a dictionary
        containing parsing results.
        """
        elements = {}
        try:
            schema_path = os.path.join(self.input_path, file)
            with open(schema_path) as xml_file:
                data = xml_file.read()
        except Exception, ex:
            print "Error occurred while opening the message profile file: ", ex
            sys.exit(1)

        try:
            f = objectify.XML(data)
        except Exception, ex:
            print "Invalid XML file: ", file, ex
            sys.exit(1)

        messageStructure = f.HL7v2xStaticDef.get('MsgStructID')

        messages = collections.defaultdict(list)

        children = self._parse_children(f.HL7v2xStaticDef, messageStructure)
        messages[messageStructure] = ('cp', 'sequence', children)

        return messages

if __name__ == '__main__':
    usage = "%prog [options] message_profile_folder"
    example = "Example: python profile_parser.py /home/user/ihe_2_3_folder"
    parser = OptionParser(usage=usage, epilog=example)
    parser.add_option("-o", "--output_dir",
                        action="store", dest="output_dir", default="./profile",
                        help="output path [%default]")
    (options, args) = parser.parse_args()
    try:
        path = args[0]
    except:
        parser.error("Please specify the folder containing message profile files.")
    else:
        if not os.path.isdir(path):
            parser.error("Folder %s not found." % path)
        ProfileParser(path, options.output_dir)
