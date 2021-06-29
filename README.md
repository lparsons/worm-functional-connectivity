# worm-functional-connectivity

Functional connectivity atlas for the C. elegans brain

Author: Francesco Randi francesco.randi@gmail.com

## Installation

1. Install from GitHub

    ```bash
    python -m pip install git+https://github.com/leiferlab/worm-functional-connectivity
    ```

## Usage

* The main class in the python module is `FunctionalAtlas`.

    * Use the `FunctionalAtlas.from_file()` method to load a pickled instance from file.

    * There are docstrings and comments for documentation.

    * The class has two main methods:

        1. `get_standard_stimulus()` to generate one of the standard stimuli
           from the parameters chosen by the user. 

        2. `get_responses()` that returns the responses that need to be
           plotted. The method `get_responses()` expects a stimulus (*e.g.*
           generated by `get_standard_stimulus()`) and either a list of neuron
           IDs whose response the user wants to plot, or a threshold to ask for
           all the responses above that threshold. See the docstring for any
           temporary behavior for this mock atlas. 