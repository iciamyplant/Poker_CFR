from azureml.core import Workspace
import urllib.request
from azureml.core.model import Model

ws = Workspace(subscription_id="18d9c045-5366-44ac-83f3-a68cb44782c5",
               resource_group="groupe-ressources",
               workspace_name="Poker-YouTubeVideo")

# Register model
#model = Model.register(ws, model_name="kuhn-poker-cfr-model", model_path="./Kuhn-Poker/first_vanilla_cfr_kuhnpoker.py")


from azureml.core.runconfig import runConfiguration

run_local = RunConfiguration()
run_local.environment.python.user_managed_dependencies = True

from azureml.core import Experiment
experiment_name='test-experiment'
experiment = Experiment(workspace=ws, name='test-experiment')

