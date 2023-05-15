os: windows
-
pilot trigger: user.vscode("editor.action.inlineSuggest.trigger")
pilot next: user.vscode("editor.action.inlineSuggest.showNext")
pilot last: user.vscode("editor.action.inlineSuggest.showPrevious")
pilot (ok|accept): user.vscode("editor.action.inlineSuggest.commit")
pilot word: user.vscode("editor.action.inlineSuggest.acceptNextWord")
pilot nope: user.vscode("editor.action.inlineSuggest.undo")
pilot cancel: user.vscode("editor.action.inlineSuggest.hide")