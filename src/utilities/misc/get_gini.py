def get_gini_impurity(probabilities):
    """
    Get Gini impurity from a probabilities list using the following expression:
        G = 1 - sum_{0}^{n - 1}(P_i)^2

    Parameters
    ----------
    - probabilities: List containing the probabilities.

    Returns
    -------
    - Gini impurity.
    """

    summation = 0
    for p_i in probabilities:
        summation += (p_i ** 2)

    return 1 - summation


def get_weighted_gini_impurity(probabilities, weight):
    """
    Get weighted Gini impurity from a probabilities list using the following expression:
        G = 1 - sum_{0}^{n - 1}(P_i)^2 * (w_i)
    Beeing [w_i = (n_elements_of_rule / total_records)]

    Parameters
    ----------
    - probabilities: List containing the probabilities.
    - weight: number of elements that satisfy the rule.

    Returns
    -------
    - weighted Gini impurity.
    """

    summation = 0
    for p_i in probabilities:
        summation += (p_i ** 2)

    return (1 - summation) * weight
