from clearml import Model


def download_models():
    model_list = Model.query_models(
        project_name='Car Numberplate Detection',
        model_name=None,
        only_published=False,
        include_archived=True
    )

    for model in model_list:
        # print(model.name)
        # if model.name == 'train':
        model.get_local_copy()

