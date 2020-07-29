import pytest
import levenshtein

@pytest.mark.parametrize("id, expected_result", [
    (0, "abcdefghijklmnopqrstuvwxyzâêîôûàèùëïüéæœçÿ"),
    (1, "abcdefghijklmnopqrstuvwxyz"),
    (2, "abcdefghijklmnñopqrstuvwxyzáéíóúü")
])
def test_alphabet_json(id, expected_result):
    assert levenshtein.alphabet_json[id]["letter"] == expected_result


@pytest.mark.parametrize("id, expected_result", [
    (0, ".,:;'!?"),
    (1, ".,:;'!?"),
    (2, ".,:;¡!¿?")
])
def test_symbol_json(id, expected_result):
    assert levenshtein.alphabet_json[id]['symbol'] == expected_result


def test_Levenshtein_class_no_parameter():
    with pytest.raises(Exception) as e_info:
        levenshtein_class = levenshtein.Levenshtein()

@pytest.mark.parametrize('letter', [
    ('a'),
    (None)
])
def test_Levenshtein_class_only_alphabet(letter):
    with pytest.raises(Exception) as e_info:
        levenshtein_class = levenshtein.Levenshtein(alphabet = letter)


@pytest.mark.parametrize('a_symbol', [
    ('?'),
    (None)
])
def test_Levenshtein_class_only_symbol(a_symbol):
    with pytest.raises(Exception) as e_info:
        levenshtein_class = levenshtein.Levenshtein(symbol = a_symbol)


@pytest.mark.parametrize('letter, a_symbol', [
    ('a', '?'),
    ('a', 'b'),
    ('?', '.')
])
def test_Levenshtein_class_mixed_params(letter, a_symbol):
    with pytest.raises(Exception) as e_info:
        levenshtein_class = levenshtein.Levenshtein(alphabet = a_symbol, symbol = letter)


@pytest.mark.parametrize('alphabet, symbol, weight_dict, language, expected_result', [
    ('a', '?', {}, None, (1, 1, 1)),
    ('a', '?', {'a': (2, 2, 2)}, 'fr-fr', (2, 2, 2)),
    ('a', '?', {'a': (1, 2, 3)}, 'fr-fr', (1, 2, 3))
])
def test_Levenshtein_class(alphabet, symbol, weight_dict, language, expected_result):
    levenshtein_class = levenshtein.Levenshtein(alphabet, symbol, weight_dict, language)
    assert levenshtein_class.weight_dict['a'] == expected_result and levenshtein_class.weight_dict['?'] == (1, 1, 1)


@pytest.mark.parametrize('source_input, target_input, expected_result', [
    ('ab', 'ab', ([[0, 1, 2],
                   [1, 0, 1],
                   [2, 1, 0]],
                    2, 2)),
    ('ab', 'ac', ([[0, 1, 2],
                   [1, 0, 1],
                   [2, 1, 1]],
                    2, 2))
])
def test_iterative_matrix(source_input, target_input, expected_result):
    metric = levenshtein.Levenshtein('a', '.')
    assert metric.iterative_matrix(source_input, target_input) == expected_result


@pytest.mark.parametrize('source_input, target_input, expected_result', [
    ('ab', 'ab', 0),
    ('ab', 'ac', 1)
])
def test_distance(source_input, target_input, expected_result):
    metric = levenshtein.Levenshtein('a', '.')
    assert metric.distance(source_input, target_input) == expected_result


@pytest.mark.parametrize('source_input, target_input, weight_dict, expected_result', [
    ('a', '', {'a': (1, 10, 100)}, 1),
    ('', 'a', {'a': (1, 10, 100)}, 10),
    ('b', 'a', {'a': (1, 10, 100)}, 11),
    ('b', 'a', {'a': (100, 200, 3)}, 3),
    ('', '', {}, 0),
])
def test_weighted_distance(source_input, target_input, weight_dict, expected_result):
    metric = levenshtein.Levenshtein('ab', '.', weight_dict)
    assert metric.distance(source_input, target_input) == expected_result