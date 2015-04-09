# XBlock MUFI
XBlock for transcribing manuscripts using MUFI font.

## TODO List:
- [ ] Write tests
- [ ] Update the `student_view`
    - [ ] `./xblockmufi/private/view.html`
        - Add content to `<div class="xblockmufi_block"></div>` element
    - [ ] `./xblockmufi/private/view.js`
        - Add logic to `XblockMufiView` function
    - [ ] `./xblockmufi/private/view.less`
        - Add styles to `.xblockmufi_block { }` block
    - [ ] `./xblockmufi/xblockmufi.py`
        - Add back-end logic to `student_view` method
- [ ] Update the `studio_view`
    - [ ] `./xblockmufi/private/edit.html`
        - Add `<LI>` entries to `<ul class="list-input settings-list">` for each new field
    - [ ] `./xblockmufi/private/edit.js`
        - Add entry for each field to `XblockMufiEdit`
    - [ ] `./xblockmufi/private/edit.less`
        - Add styles to `.xblockmufi_edit { }` block (if needed)
    - [ ] `./xblockmufi/xblockmufi.py`
        - Add entry for each field to `studio_view_save`
- [ ] Update package metadata
    - [ ] `./package.json`
        - https://www.npmjs.org/doc/files/package.json.html
    - [ ] `./setup.py`
        - https://docs.python.org/2/distutils/setupscript.html#additional-meta-data
- [ ] Update `./Gruntfile.js`
    - http://gruntjs.com/getting-started
- [ ] Update `./README.markdown`
- [ ] Write documentation
- [ ] Publish on PyPi
