name: patch-invite
on:
  push:
    branches: [main]
    paths:
      - ".github/workflows/patch-invite.yml"
permissions:
  contents: write
jobs:
  patch:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Apply invite patch
        run: |
          set -euo pipefail
          python3 .github/scripts/patch_invite.py
          grep -c "徐杨洋是小宇儿子" index.html
      - name: Commit
        run: |
          set -euo pipefail
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add index.html
          git diff --cached --quiet || git commit -m "feat: 注册邀请码支持多个并新增一条"
          git push
