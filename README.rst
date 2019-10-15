MUFI XBlock
==================

A WYSIWYG transcription tool for Medieval Manuscripts,
for use within the OpenEdX platform.

|badge-travis|
|badge-coveralls|

`Medieval Unicode Font Initiative`_

|image-poster|

The basic Submit-and-Compare and Free-Text-Response question types do
not allow students to add formatting to their answers.
`The Digging Deeper Medieval Manuscripts course`_
wanted to allow students to
transcribe manuscripts precisely, including with the original
underlining and non-Unicode characters, so we built a
customized Submit and Compare xblock. See below for an example of one of
the course's paleography exercises using the xblock.

View a `Demo Course Example`_ here.


Installation
------------


System Administrator
~~~~~~~~~~~~~~~~~~~~

To install the XBlock on your platform,
add the following to your `requirements.txt` file:

    xblock-mufi


Course Staff
~~~~~~~~~~~~

To install the XBlock in your course,
access your `Advanced Module List`:

    Settings -> Advanced Settings -> Advanced Module List

and add the following:

    xblockmufi


.. |badge-coveralls| image:: https://coveralls.io/repos/github/Stanford-Online/xblock-mufi/badge.svg?branch=master
   :target: https://coveralls.io/github/Stanford-Online/xblock-mufi?branch=master
.. |badge-travis| image:: https://travis-ci.org/Stanford-Online/xblock-mufi.svg?branch=master
   :target: https://travis-ci.org/Stanford-Online/xblock-mufi
.. |image-poster| image:: https://lagunita.stanford.edu/c4x/English/diggingdeeper2/asset/CCCC_22__164v__zoom.png
   :width: 100%
.. _Medieval Unicode Font Initiative: https://en.wikipedia.org/wiki/Medieval_Unicode_Font_Initiative
.. _The Digging Deeper Medieval Manuscripts course: https://lagunita.stanford.edu/courses/English/diggingdeeper2/Spring2015/about
.. _Demo Course Example: https://lagunita.stanford.edu/courses/StanfordOnline/OpenEdX/Demo/courseware/f3a85ee586d14fc3840e588611790d58/40d628a227774c218cedfae6b7336a02/1?activate_block_id=i4x%3A%2F%2FStanfordOnline%2FOpenEdX%2Fvertical%2F4b80f4c8ae8a40858cd62619d6034ec2
