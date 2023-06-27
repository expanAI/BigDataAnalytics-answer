from kedro.pipeline import Pipeline, node, pipeline

from .nodes import make_predictions, report_accuracy, split_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(...),
            node(...),
            node(...),
        ]
    )
