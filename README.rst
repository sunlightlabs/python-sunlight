python-sunlight
===============

This project is an attempt to unify all the Sunlight API bindings into a single
project that is clear, concise, easy to read, powerful, and fun to play with.

Currently, this project is undergoing rapid development, so production use is
not recommended yet. This should change after results can be verified a bit
more closely.

Setup
*****

Using this library is very easy - by default, python-sunlight will search for
API keys in two places. First, ``~/.sunlight.key`` will be read, and the
contents of that file will be used as the API Key. Secondly, if an enviroment
variable called ``SUNLIGHT_API_KEY`` is set, that will be used (in the case of
both being read, the enviroment variable *will* override the file.

To register for an API key, if you don't have one, please fill out the form
`here <http://services.sunlightlabs.com/accounts/register/>`_.
