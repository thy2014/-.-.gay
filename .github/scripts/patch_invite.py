import pathlib

p = pathlib.Path("index.html")
s = p.read_text(encoding="utf-8")

old1 = 'var INVITE_CODE = "#include <bits/stdc++.h>";'
new1 = 'var INVITE_CODES = ["#include <bits/stdc++.h>", "徐杨洋是小宇儿子"];'
old2 = "if(inv !== INVITE_CODE){"
new2 = "if(INVITE_CODES.indexOf(inv) < 0){"

if old1 in s:
    s = s.replace(old1, new1)
if old2 in s:
    s = s.replace(old2, new2)

assert "INVITE_CODES.indexOf" in s, "patch failed"
assert s.count("INVITE_CODES") == 2, s.count("INVITE_CODES")

p.write_text(s, encoding="utf-8")
print("patched")
