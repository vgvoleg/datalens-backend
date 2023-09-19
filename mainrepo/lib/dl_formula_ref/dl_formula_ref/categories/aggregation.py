from dl_formula_ref.localization import get_gettext
from dl_formula_ref.registry.aliased_res import (
    AliasedResourceRegistry,
    AliasedTextResource,
)
from dl_formula_ref.registry.base import FunctionDocCategory


_ = get_gettext()

CATEGORY_AGGREGATION = FunctionDocCategory(
    name="aggregation",
    description=_(
        "Aggregate functions (or aggregations) are functions that combine multiple "
        "values from a group of entries into one, thus collapsing the group into a "
        "single entry.\n"
        "\n"
        "If you add an aggregation to a dimension, it becomes a measure.\n"
        "\n"
        "{text:agg_syntax}\n"
        "{text:agg_usage_restrictions}"
    ),
    resources=AliasedResourceRegistry(
        resources={
            "agg_syntax": AliasedTextResource(
                body=_(
                    "## Syntax {#syntax}\n"
                    "\n"
                    "In most cases aggregate functions have the same syntax as regular "
                    "functions:\n"
                    "{text:agg_simple_signature}\n"
                    "\n"
                    "For advanced cases, extended syntax may be required to indicate a custom "
                    "level of detail (LOD):\n"
                    "{text:agg_extended_signature}\n"
                    "{text:agg_syntax_lod}\n"
                    "{text:agg_syntax_bfb}\n"
                )
            ),
            "agg_simple_signature": AliasedTextResource(
                body=_("```\n" "AGGREGATE_FUNCTION_NAME(arg1, [arg2, ...])\n" "```")
            ),
            "agg_extended_signature": AliasedTextResource(
                body=_(
                    "```\n"
                    "<AGGREGATE_FUNCTION_NAME>(\n"
                    "    arg1, [arg2, ...]\n"
                    "\n"
                    "    [ FIXED dim1, dim2, ...\n"
                    "    | INCLUDE dim1, dim2, ...\n"
                    "    | EXCLUDE dim1, dim2, ... ]\n"
                    "\n"
                    "    [ BEFORE FILTER BY filtered_field1, ... ]\n"
                    ")\n"
                    "```"
                )
            ),
            "agg_syntax_lod": AliasedTextResource(
                body=_(
                    "### Level of Detail (LOD) {#syntax-lod}\n"
                    "\n"
                    "Custom LOD make possible nested aggregations and aggregations over the "
                    "entire set of rows or groups that are different from the grouping at the "
                    "chart's level.\n"
                    "\n"
                    "LOD can be specified using one of three keywords:\n"
                    "- `FIXED` — data is grouped using the listed dimensions (`dim1, dim2, ...`) "
                    "regardless of the dimensions used by the chart;\n"
                    "- `INCLUDE` — the listed dimensions (`dim1, dim2, ...`) are combined with "
                    "the chart's dimensions;\n"
                    "- `EXCLUDE` — all of the chart's dimensions are used with the exception of "
                    "those listed (`dim1, dim2, ...`).\n"
                    "\n"
                    "For any of these keywords the list may have any number of dimensions, or "
                    "even be empty.\n"
                    "\n"
                    "{text:agg_syntax_lod_inheritance}\n"
                    "{text:agg_syntax_lod_examples}\n"
                    "{text:agg_syntax_lod_consistency}\n"
                )
            ),
            "agg_syntax_lod_inheritance": AliasedTextResource(
                body=_(
                    "#### Dimension Inheritance {#syntax-lod-inheritance}\n"
                    "Dimensions are inherited by nested aggregations from the ones they are "
                    "inside of. The expression\n"
                    "```\n"
                    "AVG(MAX(SUM([Sales] INCLUDE [City]) INCLUDE [Category]))\n"
                    "```\n"
                    "in a chart with the additional dimension `[Date]` is equivalent to\n"
                    "```\n"
                    "AVG(MAX(SUM([Sales] FIXED [City], [Category], [Date]) FIXED [Category], "
                    "[Date]) FIXED [Date])\n"
                    "```\n"
                    "`INCLUDE` or `EXCLUDE` without a list of dimensions results in the same "
                    "dimensions as the aggregation above or dimensions of the chart if it is the "
                    "topmost aggregation. `FIXED` without a list means that all data is "
                    "aggregated in a single group, which can be used to calculate total values.\n"
                )
            ),
            "agg_syntax_lod_examples": AliasedTextResource(
                body=_(
                    "#### LOD Examples {#syntax-lod-examples}\n"
                    "\n"
                    "- average daily sum of `[Sales]`: `AVG(SUM([Sales] INCLUDE [Date]))`;\n"
                    "- ratio of the (daily) sum of `[Sales]` to the total sum: `SUM([Sales]) / "
                    "SUM([Sales] FIXED)`;\n"
                    "- sum of `[Sales]` of all orders that are smaller than average: "
                    "`SUM_IF(SUM([Sales] INCLUDE [Order ID]), SUM([Sales] INCLUDE [Order ID]) < "
                    "AVG([Sales] FIXED))`.\n"
                )
            ),
            "agg_syntax_lod_consistency": AliasedTextResource(
                body=_(
                    "#### Dimension Compatibility {#syntax-lod-compatibility}\n"
                    "\n"
                    "If several aggregations with custom LODs are nested inside another, their "
                    "sets of dimensions must be compatible, i.e. one of them must contain all of "
                    "the others.\n"
                    "\n"
                    "Invalid expression:\n"
                    "```\n"
                    "SUM(AVG([Sales] INCLUDE [City]) - AVG([Sales] INCLUDE [Category]))\n"
                    "```\n"
                    "One of the nested aggregations has dimension `[City]`, while the other has "
                    "`[Category]`, and there is no other that would contain both of these.\n"
                    "\n"
                    "Valid expression:\n"
                    "```\n"
                    "SUM(\n"
                    "    AVG([Sales] INCLUDE [City], [Category])\n"
                    "    - (AVG([Sales] INCLUDE [City]) + AVG([Sales] INCLUDE [Category])) / 2\n"
                    ")\n"
                    "```\n"
                    "\n"
                    "One of the nested aggregations' set of dimensions contains all of the "
                    "others.\n"
                    "\n"
                    "Another important restriction for LOD is that top-level aggregations must "
                    "not contain any dimensions not used in the chart."
                )
            ),
            "agg_syntax_bfb": AliasedTextResource(
                body=_(
                    "### BEFORE FILTER BY {#syntax-before-filter-by}\n"
                    "\n"
                    "If any fields are listed in `BEFORE FILTER BY`, then this aggregate function "
                    "is calculated before data is filtered using these fields.\n"
                    "\n"
                    "`BEFORE FILTER BY` applies to all nested aggregate functions too.\n"
                    "Example:\n"
                    "- Formula — `AVG(SUM([Sales] INCLUDE [Date]) BEFORE FILTER BY [City])`.\n"
                    "- Equivalent — `AVG(SUM([Sales] INCLUDE [Date] BEFORE FILTER BY [City]) "
                    "BEFORE FILTER BY [City])`.\n"
                    "\n"
                    "Do not use conflicting `BEFORE FILTER BY` clauses:\n"
                    "- Valid: `AVG(SUM([Sales] INCLUDE [Date] BEFORE FILTER BY [City], "
                    "[Category]) BEFORE FILTER BY [City])` — functions are nested and (`[City]`) "
                    "is a subset of (`[City], [Category]`).\n"
                    "- Valid: `AVG(SUM([Sales] INCLUDE [Date] BEFORE FILTER BY [Category]) BEFORE "
                    "FILTER BY [City])` — functions are nested, so field lists are combined in "
                    "the second of the two functions.\n"
                    "- Valid: `SUM([Sales] BEFORE FILTER BY [City], [Category]) - SUM([Sales] "
                    "BEFORE FILTER BY [City])` — (`[City]`) is a subset of (`[City], "
                    "[Category]`).\n"
                    "- Not valid: `SUM([Sales] BEFORE FILTER BY [Category]) - SUM([Sales] BEFORE "
                    "FILTER BY [City])` — functions are not nested and neither of (`[Category]`) "
                    "and (`[City]`) is a subset of the other."
                )
            ),
            "agg_usage_restrictions": AliasedTextResource(
                body=_(
                    "## Usage Restrictions {#usage-restrictions}\n"
                    "\n"
                    "There are the following features of using aggregations:\n"
                    "1. A function or operator cannot have aggregate and non-aggregate "
                    "expressions as its arguments simultaneously. The following usage is "
                    "forbidden: `CONCAT([Profit], SUM([Profit]))`.\n"
                )
            ),
        }
    ),
    keywords=_("aggregate functions,aggregations,aggregate data,level of detail,lod"),
)
