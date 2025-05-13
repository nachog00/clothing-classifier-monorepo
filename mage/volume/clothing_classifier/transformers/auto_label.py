if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd

@transformer
def transform(df, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """

    # Safety check: convert list to DataFrame if needed
    if isinstance(df, list):
        df = pd.DataFrame(df)

    def categorize_value(value):
        value = str(value).lower()

        keywords = {
            'upper_body': ['campera', 'saco', 'remera', 'blusa', 'camisa'],
            'lower_body': ['pantalon', 'short', 'jean', 'bermuda'],
            'footwear': ['zapatilla', 'bota', 'botin', 'sandalia'],
            'accessories': ['mochila', 'bolso', 'cinturon', 'gorra'],
        }

        for category, terms in keywords.items():
            if any(term in value for term in terms):
                return category

        return None

    # Apply function to the column
    df["label"] = df["identificador_de_url"].map(categorize_value)

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
