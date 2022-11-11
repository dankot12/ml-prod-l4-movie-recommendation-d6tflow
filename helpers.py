"""
Dummy helper function to show the decision behind deploying
a particular model (least RMSE in this case).
"""
def deploy_least_rmse_model(models, model_scores):
    min_score = float('inf')
    selected_model = None
    for model in models.keys():
        if model_scores[model] < min_score:
            selected_model = model
            min_score = model_scores[model]
    print(f"The model with least RMSE is deployed which is {selected_model}")
