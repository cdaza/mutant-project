from ..utils.redis_utils import get_dict_from_key


def get_stats():
    stats_key = 'stats'
    stats = get_dict_from_key(stats_key)
    count_mutant_dna = int(stats[b'count_mutant_dna'])
    count_human_dna = int(stats[b'count_human_dna'])

    if count_mutant_dna and count_human_dna:
        ratio = round(float(count_mutant_dna / count_human_dna), 2)

    return {
        'count_mutant_dna': count_mutant_dna,
        'count_human_dna': count_human_dna,
        'ratio': ratio
    }
