TheySay AffectR API Python Client
=================================

The TheySay AffectR API Python client provides a simple interface to the [TheySay AffectR API](http://api.theysay.io).

You can sign up for a TheySay AffectR API account at http://theysay.io.

### Requirements

Python 2.7 or later.

### Getting Started

Set your account details:

```python
affectr.set_details("your username", "your password")
```

Next, call any classification task with your text on the AffectR API class, for example:

```python
affectr.client.classify_intent(
    "We are planning to implement a real-time data service. " +
    "What are the advantages/disadvantages of using a Foobar-compliant database over Hype.js?"
)[0].intentType)
```

For more information, please visit http://docs.theysay.apiary.io/.

Copyright 2013 TheySay Ltd. All rights reserved.
