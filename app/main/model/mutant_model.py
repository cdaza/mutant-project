from flask_restx import Namespace, fields


class MutantModel:
    api = Namespace('Mutant', description="Service to detect Mutants")

    dna = api.model(
        'ModelDNA', dict(
            dna=fields.List(fields.String(required=True, description='DNA sequence')),
        ))
