from os.path import join
from sys import argv


def _get_template_content():
    """
    Get content of template Jenkinsfile.
    :return: Template Jenkinsfile content
    """
    with open(join(project_root_path, "tools/resources/CarelessVaquitaTestPipelineStageTemplate"), mode="r") \
            as template:
        return template.readlines()


def _get_injection_index(jenkinsfile_content):
    """
    Get index of template code injection by finding 'stages' line number in main Jenkinsfile.
    :param jenkinsfile_content: Main Jenkinsfile content
    :return: Index of template code injection
    """
    for index, line in enumerate(jenkinsfile_content):
        if "stages" in line:
            return index + 1


def generate_test_jenkinsfile():
    """
    Generate TestJenkinsfile by injecting template code (available in CarelessVaquitaTestPipelineStageTemplate) in
    line provided by _get_injection_index function.
    :return: None
    """
    with open(join(project_root_path, "Jenkinsfile"), mode="r") as main_jenkinsfile:
        jenkinsfile_content = main_jenkinsfile.readlines()
        jenkinsfile_content.insert(_get_injection_index(jenkinsfile_content), "".join(_get_template_content()))
    with open(join(project_root_path, "tools/jenkins/CarelessVaquitaTestJenkinsfile"), mode="w") as test_jenkinsfile:
        test_jenkinsfile.writelines(jenkinsfile_content)


if __name__ == '__main__':
    project_root_path = argv[1]
    generate_test_jenkinsfile()
    print("Generated tools/jenkins/CarelessVaquitaTestJenkinsfile")
