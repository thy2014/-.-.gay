# 游戏站（GitHub Pages 部署）

一个纯静态的游戏站：主页有登录（内置账号，无注册）+ 游戏库，点卡片进入游戏。
第一个游戏是《割草肉鸽》——类吸血鬼幸存者，自动攻击、升级三选一卡牌强化、血量与经验成长、按账号自动存档。

## 项目结构

```
new-chat/
├─ index.html          # 主页：登录 + 游戏库
├─ games/
│  ├─ roguelike.html   # 割草肉鸽游戏（第一个游戏）
│  └─ games.json       # 游戏清单（主页读取）
└─ README.md           # 本说明
```

## 账号（写死在 index.html 里，只登录不注册）

| 账号     | 密码       |
|----------|-----------|
| thy2014  | thy20141005 |
| GHBQU    | GHBQU     |
| lyb2015  | lyb2015   |
| lcx2015  | lcx2015   |

登录状态存在浏览器 localStorage（`gstation_session`），换浏览器/清缓存要重新登录。
游戏的存档按账号分开存（`gr_roguelike_save_<账号>`、`gr_roguelike_rec_<账号>`），换账号互不影响。

## 本地预览

直接双击 `index.html` 也能看（用内置的游戏列表），但"游戏库自动扫描"和"games.json"这类联网功能在 file:// 下不可用。
想完整体验，在本目录起个本地服务再访问：

```bash
# 方式一：python
python -m http.server 8080

# 方式二：node（装了 node 就用这个）
npx -y serve .
```

然后浏览器打开 `http://localhost:8080`。

## 部署到 GitHub Pages

1. 在 GitHub 建一个仓库（建议用你已有的 `-.-.gay`）。
2. 把本项目所有文件推到仓库（根目录直接放 index.html 和 games/）。
3. 仓库 Settings → Pages → Build and deployment：
   - Source 选 **Deploy from a branch**
   - Branch 选 **main**，目录选 **/ (root)**，Save。
4. 等一两分钟，Pages 会把代码发布成网站。
5. 默认访问地址是 `https://<用户名>.github.io/<仓库名>/`。

## 绑定自定义域名（你的 `徐杨洋是我儿子.是.gay`）

1. 仓库 Settings → Pages → **Custom domain** 输入 `徐杨洋是我儿子.是.gay` → Save。
   GitHub 会校验 DNS，成功后在仓库里自动生成一个 `CNAME` 文件（内容是域名，不用手动管）。
2. 在域名服务商（你截图那个 DNS 页面）加 **4 条 A 记录**，内容分别是：

   ```
   185.199.108.153
   185.199.109.153
   185.199.110.153
   185.199.111.153
   ```

   名称 `@`、类型 `A`、TTL 300（你已经加好了）。
3. 等解析生效（几分钟到几小时），访问 `徐杨洋是我儿子.是.gay` 就是你的游戏站。

> 绑定自定义域名时页面出现 **404**：说明域名已经解析到 GitHub Pages 了，只是仓库里还没有文件。
> 把上面第 2 步的文件推上去、Pages 重新构建后就好了。

## 关于"GitHub 代理 / 加速"

- **绑定域名这步本身不需要代理**，就是 A 记录直接指向 GitHub 的 IP。
- 境内直连 GitHub Pages 有时慢/偶尔打不开。可选方案：
  1. 套 **Cloudflare**（免费 CDN）：在 Cloudflare 添加站点 → 改 DNS 到 Cloudflare → 它自动做反代加速，还能套 HTTPS。这是最省事的加速方案。
  2. GitHub API 自动扫描如果被墙，改 `index.html` 里 `GH.api` 为可用的 API 加速地址。
  3. 用国内静态托管（Gitee Pages / Coding / 腾讯云 COS + CDN）做镜像站，域名 CNAME 到那边。

## 怎么添加新游戏（重点）

**方式一：自动扫描（推荐，符合"丢个 html 就显示"）**

往 `games/` 文件夹里丢一个 HTML 文件（例如 `games/俄罗斯方块.html`），主页会自动通过 GitHub API 扫描 `games/` 目录，把它显示成一张游戏卡。前提：
- 仓库是 public（GitHub Pages 免费版强制 public）。
- `index.html` 顶部 `GH` 配置里的 `owner` / `repo` 写对。
- 这个文件你自己能通过 `https://github.com/<owner>/<repo>/blob/main/games/<文件名>` 访问到（自动扫描用的就是这个接口）。

**方式二：清单（最稳，不依赖 GitHub API）**

往 `games/` 丢 HTML 后，再在 `games/games.json` 里加一行：

```json
{ "id": "newgame", "title": "新游戏名", "desc": "一句话介绍", "file": "games/新游戏.html", "tag": "标签" }
```

两种方式都会和内置列表合并、去重，不会重复显示。

## 割草肉鸽游戏说明

- 操作：**WASD / 方向键** 移动，**自动攻击**；手机触屏左半区拖动 = 虚拟摇杆。
- 血条：左上角；经验条：底部；右上角显示时间 / 击杀 / 得分。
- **升级**：击杀敌人掉落经验晶石，拾取累积经验，升级后**三选一卡牌**强化（生命、移速、火力、攻速、弹幕、穿透、暴击、经验加成、环绕、激光、散射等 14 种）。
- **存档**：开局自动判断有没有存档，有就提示"继续上次存档"；游戏中每 5 秒 + 切走页面时自动存档；死亡后记录最佳成绩并清除本局存档。
- **P / Esc** 暂停。
