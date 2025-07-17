import pandas as pd
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder

# WL


def encode_dataframe(
    df,
    categorical_vars=None,
    ordinal_vars=None,
    ohe_list=None,
    oe_list=None,
    add_intercept=False,
):
    """
    Encode specified categorical and ordinal variables in a DataFrame.

    Args:
        - df: pandas.DataFrame containing the data to be encoded.
        - categorical_vars: list of column names to be one-hot-encoded or None.
        - ordinal_vars: list of column names to be ordinal-encoded or None.
        - ohe_list: list of OneHotEncoder objects pre-configured for encoding the respective categorical_vars or None.
        - oe_list: list of OrdinalEncoder objects pre-configured for encoding the respective ordinal_vars or None.
        - add_intercept: bool indicating whether to add an intercept column to the DataFrame (default False).

    Returns:
        - new_df: pandas.DataFrame with specified encodings applied and original columns dropped if applicable.
    """
    if categorical_vars is not None and ohe_list is not None:
        if len(categorical_vars) != len(ohe_list):
            raise ValueError(
                "The number of categorical variables must match the number of OneHotEncoders."
            )

    if ordinal_vars is not None and oe_list is not None:
        if len(ordinal_vars) != len(oe_list):
            raise ValueError(
                "The number of ordinal variables must match the number of OrdinalEncoders."
            )

    new_df = df.copy()

    # One-hot-encode the specified categorical variables if provided
    if categorical_vars is not None and ohe_list is not None:
        for var, ohe in zip(categorical_vars, ohe_list):
            # fit the encoder and transform the data (returns a sparse matrix)
            encoded_data = ohe.fit_transform(new_df[[var]]).toarray()
            # retrieve categories for naming the one-hot-encoded columns
            categories = ohe.categories_[0]

            # create column names using the variable name and category labels
            new_cols = [f"{var}_{category}" for category in categories]
            # add one-hot-encoded columns to the dataframe
            new_df[new_cols] = encoded_data
            # drop the original categorical column
            new_df.drop(var, axis=1, inplace=True)

    # ordinal-encode the specified ordinal variables if provided
    if ordinal_vars is not None and oe_list is not None:
        for var, oe in zip(ordinal_vars, oe_list):
            # fit the encoder and transform the data
            encoded_data = oe.fit_transform(new_df[[var]])

            # replace the original column with the encoded data
            new_df[var] = encoded_data.astype(int)

    # optionally, add an intercept column (constant value of 1)
    if add_intercept:
        new_df.insert(0, "Intercept", 1)

    return new_df


# # Toy data
# df = pd.DataFrame({
#     'Sales': [9.50, 11.22, 10.06, 7.40, 4.15],
#     'CompPrice': [138, 111, 113, 117, 141],
#     'Income': [73, 48, 35, 100, 64],
#     'Advertising': [11, 16, 10, 4, 3],
#     'Population': [276, 260, 269, 466, 340],
#     'Price': [120, 83, 80, 97, 128],
#     'ShelveLoc': ['Bad', 'Good', 'Medium', 'Medium', 'Bad'],
#     'Age': [42, 65, 59, 55, 38],
#     'Education': ['high', 'bachelor','bachelor', 'grad', 'high'],
#     'Urban': ['Yes', 'Yes', 'Yes', 'Yes', 'No'],
#     'US': ['Yes', 'Yes', 'Yes', 'Yes', 'No']
# })

# # Specify the encoding for the 'Education' column
# education_ordering = [['high', 'bachelor', 'grad']]
# oe_list = [OrdinalEncoder(categories=education_ordering)]

# # Specify the encoding order for 'ShelveLoc' and 'US' columns
# shelveloc_ordering = [['Bad', 'Medium', 'Good']]
# us_ordering = [['No', 'Yes']]
# urban_ordering = [['No', 'Yes']]
# # Create list of OneHotEncoder objects with specified category orderings
# ohe_list = [
#     OneHotEncoder(categories=shelveloc_ordering),
#     OneHotEncoder(categories=us_ordering),
#     OneHotEncoder(categories=urban_ordering )
# ]


# encoded_df = encode_dataframe(
#     df,
#     categorical_vars=['ShelveLoc', 'Urban', 'US'], # list of categorical columns
#     ordinal_vars=['Education'],  # list of ordinal columns
#     ohe_list=ohe_list, # matching list of OneHotEncoders
#     oe_list=oe_list, # matching list of OrdinalEncoders
#     add_intercept=True # include intercept column
# )

# print(encoded_df)
