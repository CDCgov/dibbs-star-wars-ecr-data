from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import json
from utils import generate_uuid, generate_timestamp
import argparse

parser = argparse.ArgumentParser(description='Generate ECR XML file from a given mapping json file.')
parser.add_argument('-m', '--mapping', type=str, help='File name of mapping json file, will default to mon-mothma-covid.json')
args = parser.parse_args()
mapping_file = "mon-mothma-covid.json"

if args.mapping:
  mapping_file = args.mapping

# Setup the Jinja environment to load templates
env = Environment(
    loader=FileSystemLoader(
        Path(__file__).resolve().parent.parent / "assets" / "templates"
    )
)

env.globals['uuid'] = generate_uuid
env.globals['timestamp'] = generate_timestamp

# Load the specific template file
template = env.get_template('components/base.xml.j2')

# Define the data you want to inject
base_path = Path(__file__).resolve().parent.parent
json_path = base_path / "assets" / "mappings" / mapping_file
with open(json_path) as f:
    data = json.load(f)

# Set globals from data
env.globals['codeSystems'] = data["codeSystems"]

env.globals['lab_results_repetitions'] = 1
env.globals['encounters_diagnosis_repetitions'] = 1
env.globals['history_of_present_illness_repetitions'] = 1
env.globals['problems_obs_repetitions'] = 1
env.globals['medications_administered_repetitions'] = 1
env.globals['immunization_activities_repetitions'] = 1
env.globals['plan_of_treatment_repetitions'] = 1

if 'config' in data :
  if 'lab_results_repetitions' in data['config']:
    env.globals['lab_results_repetitions'] = data['config']['lab_results_repetitions']
  if 'encounters_diagnosis_repetitions' in data['config']:
    env.globals['encounters_diagnosis_repetitions'] = data['config']['encounters_diagnosis_repetitions']
  if 'history_of_present_illness_repetitions' in data['config']:
    env.globals['history_of_present_illness_repetitions'] = data['config']['history_of_present_illness_repetitions']
  if 'problems_obs_repetitions' in data['config']:
    env.globals['problems_obs_repetitions'] = data['config']['problems_obs_repetitions']
  if 'medications_administered_repetitions' in data['config']:
    env.globals['medications_administered_repetitions'] = data['config']['medications_administered_repetitions']
  if 'immunization_activities_repetitions' in data['config']:
    env.globals['immunization_activities_repetitions'] = data['config']['immunization_activities_repetitions']
  if 'plan_of_treatment_repetitions' in data['config']:
    env.globals['plan_of_treatment_repetitions'] = data['config']['plan_of_treatment_repetitions']

xml_nsmap = {
        None: "urn:hl7-org:v3",
        "xsi": "http://www.w3.org/2001/XMLSchema-instance",
        "sdtc": "urn:hl7-org:sdtc",
        "voc": "http://www.lantanagroup.com/voc",
        "schema_location": "urn:hl7-org:v3 ../../schema/infrastructure/cda/CDA_SDTC.xsd"
    }

# Render the template with your data
rendered_xml = template.render(data, nsmap=xml_nsmap)

# Save the output to a new XML file - TODO: re-enabled timestamped filenames
#output_filename = mapping_file.replace(".json", "-"+generate_timestamp(None, True)+".xml")
output_filename = mapping_file.replace(".json", ".xml")
with open(output_filename, "w", encoding="utf-8") as f:
    f.write(rendered_xml)

print("XML file [" + output_filename + "] generated successfully!")
