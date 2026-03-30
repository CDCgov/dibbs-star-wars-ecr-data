# Star Wars - ECR Data Generator 

General disclaimer - This repository was created for use by CDC programs to collaborate 
on public health related projects in support of the CDC mission. 
GitHub is not hosted by the CDC, but is a third party website used by CDC and its partners 
to share information and collaborate on software. CDC use of GitHub does not imply an endorsement 
of any one particular service, product, or enterprise.

## Overview

This repository contains templates and script to aid in generating synthetic ECR data for the purposes
of testing other systems. 

### Components
ECRs are generated using Jinja2 templates which are located under `assets/templates`.
Files under `assets/mappings` are JSON data files that will feed into these template files via the
`scripts/generate_ecr.py` script which reads the JSON data file, sets up the Jinja2 environment, sets 
some additional globals, and renders the base template (`assets/templates/components/base.xml.j2`).

### Setup
- Clone this repo
- Install Python > 3.12
- Install pip-tools (replace the `x` with the actual version of Python you have)
    
    ```
    > pip3.x install pip-tools
    ```
    
- Compile TOML file (generates a requirement.txt file)
    
    ```
    > python3.x -m piptools compile pyproject.toml
    ```
    
- Install dependencies
    
    ```
    > pip3.x install -r requirements.txt
    ```

### How to generate a test ECR
Use an existing JSON mapping data file in `assets/mappins` or create your own. 
Most sections are required except the `config` section which includes configs on repeatable
resources for generating very large ECRs (usually needed for performance and load testing).

To generate an ECR using the default `mon-mothma-covid.json` data file simply go to the `scripts` dir and run:
```
> generate_ecr.py
```

To use another data file use the `-m` arg (which will look for the file in the `assets/mappings` folder):
```
> generate_ecr.py -m <filename>.json
```
The file will be written to the `scripts` folder named `<data_filename>-<timestamp>.xml`.
 
## Future Improvements
This is just an initial version but the main goal was to make the data mapping JSON files 
be much easier to update than editing an ECR xml directly so please keep this in mind when making changes.

### Future improvements can include (but are not limited to):
- Randomly generating data (instead of just repeating it)
  - This could include adding lookup files for codeSystems so that we can randomly choose from them (needs some thought)
- Trigger codes needs to be supported properly (this includes sdtc fields)
- Create a macro for codes
- Timestamps and status codes are not templated - should they be? 
- Address `TODO`s which include
  - Sections that still need to be templated
  - Initial Case Report Trigger Code template ids
  - Travel History needs to be an array of data

## Standard Notices

### Public Domain Standard Notice
This repository constitutes a work of the United States Government and is not
subject to domestic copyright protection under 17 USC § 105. This repository is in
the public domain within the United States, and copyright and related rights in
the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).
All contributions to this repository will be released under the CC0 dedication. By
submitting a pull request you are agreeing to comply with this waiver of
copyright interest.

### License Standard Notice
The repository utilizes code licensed under the terms of the Apache Software
License and therefore is licensed under ASL v2 or later.

This source code in this repository is free: you can redistribute it and/or modify it under
the terms of the Apache Software License version 2, or (at your option) any
later version.

This source code in this repository is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the Apache Software License for more details.

You should have received a copy of the Apache Software License along with this
program. If not, see http://www.apache.org/licenses/LICENSE-2.0.html

The source code forked from other open source projects will inherit its license.

### Privacy Standard Notice
This repository contains only non-sensitive, publicly available data and
information. All material and community participation is covered by the
[Disclaimer](DISCLAIMER.md)
and [Code of Conduct](code-of-conduct.md).
For more information about CDC's privacy policy, please visit [http://www.cdc.gov/other/privacy.html](https://www.cdc.gov/other/privacy.html).

### Contributing Standard Notice
Anyone is encouraged to contribute to the repository by [forking](https://help.github.com/articles/fork-a-repo)
and submitting a pull request. (If you are new to GitHub, you might start with a
[basic tutorial](https://help.github.com/articles/set-up-git).) By contributing
to this project, you grant a world-wide, royalty-free, perpetual, irrevocable,
non-exclusive, transferable license to all users under the terms of the
[Apache Software License v2](http://www.apache.org/licenses/LICENSE-2.0.html) or
later.

All comments, messages, pull requests, and other submissions received through
CDC including this GitHub page may be subject to applicable federal law, including but not limited to the Federal Records Act, and may be archived. Learn more at [http://www.cdc.gov/other/privacy.html](http://www.cdc.gov/other/privacy.html).

### Records Management Standard Notice
This repository is not a source of government records, but is a copy to increase
collaboration and collaborative potential. All government records will be
published through the [CDC web site](http://www.cdc.gov).

### Additional Standard Notices
Please refer to [CDC's Template Repository](https://github.com/CDCgov/template) for more information about [contributing to this repository](https://github.com/CDCgov/template/blob/main/CONTRIBUTING.md), [public domain notices and disclaimers](https://github.com/CDCgov/template/blob/main/DISCLAIMER.md), and [code of conduct](https://github.com/CDCgov/template/blob/main/code-of-conduct.md).

## Related documents

* [Open Practices](open_practices.md)
* [Rules of Behavior](rules_of_behavior.md)
* [Thanks and Acknowledgements](thanks.md)
* [Disclaimer](DISCLAIMER.md)
* [Contribution Notice](CONTRIBUTING.md)
* [Code of Conduct](code-of-conduct.md)