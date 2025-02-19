from mp_api.core.client import BaseRester
from mp_api.routes.similarity.models import SimilarityDoc


class SimilarityRester(BaseRester):

    suffix = "similarity"
    document_model = SimilarityDoc  # type: ignore
    primary_key = "task_id"
