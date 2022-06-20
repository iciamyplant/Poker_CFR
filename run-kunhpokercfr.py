from azureml.core import Experiment
from azureml.core import Workspace, Environment
from azureml.core import ScriptRunConfig



#connect to my workspace
ws = Workspace(subscription_id="18d9c045-5366-44ac-83f3-a68cb44782c5",
               resource_group="groupe-ressources",
               workspace_name="Poker-YouTubeVideo")

#creer une experiment
experiment_name = 'my_experiment'
experiment = Experiment(workspace=ws, name=experiment_name)

#select a 
#configuration dexecution du script
ws = Workspace.from_config()

myenv = Environment.get(workspace=ws, name="AzureML-Minimal")

myscript = ScriptRunConfig(source_directory = './Kuhn-Poker',script ='first_vanilla_cfr_kuhnpoker.py',
compute_target = 'compute-poker', environment = myenv)

myscript.run_config.target = 'compute-poker'

run = experiment.submit(config=myscript)
run.wait_for_completion(show_output=True)