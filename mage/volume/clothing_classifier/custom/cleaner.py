if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(df,*args, **kwargs):
    """
    args: The output from any upstream parent blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Clean numeric fields with comma thousands separator
    def clean_number(s):
        try:
            return float(str(s).replace(",", "").strip())
        except ValueError:
            return None

    for col in ['precio', 'Precio promocional']:
        if col in df.columns:
            df[col] = df[col].apply(clean_number)

    return df


    return {}


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
