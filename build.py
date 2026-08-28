# -*- coding: utf-8 -*-
"""训练营 9 个 Day 页面生成脚本：从模板复制并替换标题/配色/logo/footer/md"""
import io, os

SRC = r'C:\Users\Chrisgao\Claude-Code安装指南.html'
BASE = r'C:\Users\Chrisgao\training-camp'

# 附件 URL 前缀
DL = 'https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code='

TITLE_OLD = '<title>Claude Code 安装整合指南（Windows 11）</title>\n<meta name="description" content="整合 codetaste.com/setup 与 cc.obuudo.com 的 Claude Code 安装说明，Windows 11 小白保姆级教程。">'
LOGO_OLD = '''    <div class="logo">
      <svg class="logo-mark" viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="6" fill="var(--accent)"/><path d="M8.5 9l3 3-3 3M13.5 15H16" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      <span>Claude Code 安装指南</span>
      <span class="badge">Windows</span>
    </div>'''
LOGO_NEW = '''    <div class="logo">
      <svg class="logo-mark" viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="6" fill="var(--accent)"/><text x="12" y="16.5" text-anchor="middle" font-family="'JetBrains Mono',monospace" font-size="11" font-weight="800" fill="#fff">CC</text></svg>
      <span>Claude Code 训练营</span>
    </div>'''
FOOTER_OLD = '''<footer class="footer">
  整合来源：<a href="https://codetaste.com/setup/">CodeTaste</a> · <a href="https://cc.obuudo.com/">cc.obuudo.com（火箭叔 Alex）</a> · 生成于 2026-08-28
</footer>'''
FOOTER_NEW = '''<footer class="footer">
  <a href="index.html">← 返回训练营目录</a> · Claude Code 训练营 · 生成于 2026-08-28
</footer>'''

COLOR_OLD = '''  :root {
    --accent: #b45309;
    --accent-strong: #92400e;
    --accent-soft: #fdf4e7;
    --bg: #f6f5f3;
    --card: #ffffff;
    --text: #1c1917;
    --text-dim: #78716c;
    --border: #e7e5e4;
    --border-strong: #d6d3d1;
    --code-bg: #1c1917;
    --code-text: #e7e5e4;
    --shadow: 0 1px 2px rgba(28,25,23,.05);
    --radius: 12px;
  }
  [data-theme="dark"] {
    --accent: #e0954d;
    --accent-strong: #f0b078;
    --accent-soft: #2b2117;
    --bg: #131210;
    --card: #1b1a18;
    --text: #e7e5e4;
    --text-dim: #a8a29e;
    --border: #2c2a27;
    --border-strong: #3d3a36;
    --code-bg: #0f0e0d;
    --code-text: #e7e5e4;
    --shadow: 0 1px 2px rgba(0,0,0,.4);
  }'''
COLOR_NEW = '''  :root {
    --accent: #1e40af;
    --accent-strong: #1e3a8a;
    --accent-soft: #e8effc;
    --bg: #f6f7f9;
    --card: #ffffff;
    --text: #181b23;
    --text-dim: #6b7280;
    --border: #e4e7eb;
    --border-strong: #cfd5dd;
    --code-bg: #1b2130;
    --code-text: #e8ecf4;
    --shadow: 0 1px 2px rgba(15,23,42,.05);
    --radius: 12px;
  }
  [data-theme="dark"] {
    --accent: #60a5fa;
    --accent-strong: #93c5fd;
    --accent-soft: #15233c;
    --bg: #10141c;
    --card: #181e29;
    --text: #e8ecf4;
    --text-dim: #9aa4b3;
    --border: #293140;
    --border-strong: #3a4354;
    --code-bg: #0c1017;
    --code-text: #e8ecf4;
    --shadow: 0 1px 2px rgba(0,0,0,.4);
  }'''

VIDEO = '''📹 **课程视频**（视频文件待添加，稍后嵌入）。

> 💡 视频由训练营提供，收到视频文件后本页会直接内嵌播放器。'''

def link(name, code, ext=''):
    return '[%s](%s%s)' % (name, DL, code)

pages = [
# ---------------- Day0 ----------------
('day0.html', 'Day0 - Claude Code 预热教程',
 '训练营第一课：把 Claude Code 跑通。',
 f'''# Day0 - Claude Code 预热教程

> 训练营第一课：先把 Claude Code 装好，走通完整教程。

## 课程内容

访问 [codetaste.com/setup](https://codetaste.com/setup/) 的安装教程，按照每一步走完完整的安装流程。

## 预热作业

完成下面 2 个预热作业：

1. **牛刀小试**：下载作业 PDF，按步骤完成第一次任务
   - {link('📄 预热任务：第一次牛刀小试.pdf', 'ZjcxMzFlN2Y0NGNhNjQ2MWY4MTVkMTE2NzJjZWFiODRfY2VjMmMyNTQ4MTAyOGNjZjA3NDc1MTdmYmNlMmE2MmFfSUQ6NzY2MDA5MjIzODUxNjkzMTc2Ml8xNzg3OTAxNjQzOjE3ODc5MDUyNDNfVjM')}
2. **安装飞书到 Claude Code**：下载作业 PDF，完成飞书接入
   - {link('📄 安装飞书到 Claude Code - 预热课程.pdf', 'ZjIyOTlhZTg0MzI1MzE0NGZmMjA2MTI3YTIyZTU4M2RfYmZjMTY5MWM1MjA1NzZiNjMxM2UzZjBiZDJlMWQ0MzhfSUQ6NzY2MDA5MjIzNjQ5MTcyMTk0OV8xNzg3OTAxNjQzOjE3ODc5MDUyNDNfVjM')}

## 软件下载（如官方下载慢，可用这里）

- {link('⬇️ CC-Switch v3.16.3 Windows (.msi)', 'ODJiMTcwYzRhZGRkOTEzMWQ5YjRmYzkzMzZmOTgzNWFfMTU0Njc1MDVkNWIzOWRhZmRmYjg1MTMxZmMyMDdhMjlfSUQ6NzY2MDA5Mzk0OTE3MjE0MTAwNl8xNzg3OTAxNjQzOjE3ODc5MDUyNDNfVjM')}
- {link('⬇️ CC-Switch v3.16.3 macOS (.dmg)', 'ZTA5YmUxZDcyOGZlMjdlODAxYTY1OTc3NDkzNzg0ODZfMTBkMGE1MjE0ZWZlNmI3ZWZhNWU4YjQyZmEzZWFmOTdfSUQ6NzY2MDA5Mzk0OTI2MDQ5OTkyOF8xNzg3OTAxNjQzOjE3ODc5MDUyNDNfVjM')}

## 完成后

按顺序学习，并在群里完成作业并打卡。每天做到多次观看，熟练掌握。'''),

# ---------------- Day1-1 ----------------
('day1-1.html', 'Day 1-1 快速入门 Claude Code 与基础操作',
 '15 分钟认识住在你电脑里的 AI 助理。',
 f'''# Day 1-1 快速入门 Claude Code 与基础操作

> 欢迎来到第一堂课！没有编程基础也能轻松上手。今天用 15 分钟快速认识 Claude Code，并掌握最基础操作。

## 本课内容

- 改用**语音输入法**，像跟真人交代工作一样和 AI 高质量沟通
- 在桌面建一个**专用文件夹**，给 AI 助理安个家
- 打第一个招呼，并学会一个最基础的自动化「小技能（Skill）」

{VIDEO}

## 课后

按顺序学习，并在群里完成作业并打卡。'''),

# ---------------- Day1-2 ----------------
('day1-2.html', 'Day 1-2 Claude Code 核心概念与进阶操作',
 '掌握核心概念：技能库、规则文件 CLAUDE.md、虚拟团队。',
 f'''# Day 1-2 Claude Code 核心概念与进阶操作

> 恭喜你通关第一课！这堂课带你掌握 Claude Code 的核心概念与进阶操作。

## 本课内容

- 像整理抽屉一样把你的**技能库**分类放好，通用技能随时随地一键调出
- 核心概念「**规则文件** `CLAUDE.md`」——一张写给 AI 的"禁止犯错清单"
- 解锁高阶操作：让一个 AI 变身成多人的「**虚拟团队（Agent Team）**」，分工合作干活

{VIDEO}

## 课后

按顺序学习，并在群里完成作业并打卡。'''),

# ---------------- Day2 ----------------
('day2.html', 'Day2 定义一个 Skill - 亚马逊信息爬取',
 '第一次学会在一线实操中封装一个 Skill。',
 f'''# Day2 定义一个 Skill - 亚马逊信息爬取

> 这是录播课的第一次作业。学会定义一个亚马逊商品信息爬取的 Skill，用于竞品监控每天的价格。

## 课程内容

- 学习怎么定义一个亚马逊一线实操的 Skill
- 对亚马逊商品页面进行数据抓取，用于竞品监控
- 第一次学会如何在一线实操环境中封装一个 Skill

## 作业完成要求

1. 根据要求完成所有提到的软件安装，**尤其是 TT Bridge**
2. 复刻整个 Skill 的封装过程，成功拿到亚马逊页面的商品价格信息并截图

## 安装 TT Bridge 的文件

把下面三个文件下载到本地后，直接丢给 Claude Code，然后说：

> 我是一个小白，现在请你看这两个压缩包和这个 PDF 文件的内容，根据里面的要求，帮我安装好 TT Bridge 这个 skill。

- {link('⬇️ tt-bridge.zip', 'ZDFkMDczYWUwMjExNTE0MDdlNDQyMDJlNjE1MGZkOWZfNjEwYTcwYzZkODg0MmUwYTVjNDQwMmIxOTBmOTE0MTlfSUQ6NzY2MDA5MjczNTAzMDU2MTk5OV8xNzg3OTAxNzE3OjE3ODc5MDUzMTdfVjM')}
- {link('⬇️ chrome-extension.zip', 'ZTBkN2NhNmI4OTIwNTkyODM4NTJhNWNlMDk3YTk2NDVfNWQ4NDUyOGEyNDNlOGVhZDhiZDFjZGEzMDUzZTM3YWZfSUQ6NzY2MDA5MjczNTY4NDk4ODA4OV8xNzg3OTAxNzE3OjE3ODc5MDUzMTdfVjM')}
- {link('📄 训后作业说明.pdf', 'N2YwYzQ3N2JiMWFlMzhjN2MzYjRhYTQ4MjZmMTU5YTZfNzViY2E1NGY5Yzg4ODhhMzdiOWIwMzZiNzBlMDc1YjJfSUQ6NzY2MDA5MjczNzUyMTcwMDA2Ml8xNzg3OTAxNzE3OjE3ODc5MDUzMTdfVjM')}

{VIDEO}

## 课后

按顺序学习，并在群里完成作业并打卡。'''),

# ---------------- Day3 ----------------
('day3.html', 'Day3 - 和飞书表格的联动和数据抓取',
 '在 Skill 封装基础上更进一步，接入飞书能力。',
 f'''# Day3 - 和飞书表格的联动和数据抓取

> 第二次作业。在 Skill 封装的基础上更进一步，把 Claude Code 和飞书表格联动起来。

## 课前准备

为了做这次作业，你需要提前安装好飞书的能力，接入 Claude Code：

- {link('📄 安装飞书到 Claude Code.pdf', 'YTI1Zjg3ZTMxNWEwY2ZhMGIyZWE2NGYzNmU4MGYwMWJfNTMxN2Y3MjE3YjZmZGFiYjQ3ZDA3ZGZhOWQ1MjAwZTBfSUQ6NzY2MDA5NTk3ODQ2MDg3NTk5M18xNzg3OTAxNzE2OjE3ODc5MDUzMTZfVjM')}

安装完成后，开始今天的学习。

## 作业要求

完整复刻通过**唤醒 Skill** 的方式启动一次竞品价格监控的爬取过程，并把内容保存到飞书表格。

{VIDEO}

## 课后

按顺序学习，并在群里完成作业并打卡。'''),

# ---------------- Day4 ----------------
('day4.html', 'Day4 - 浏览器自动化爬取信息',
 '浏览器自动化是 Agent 设计中不可跳过的一环。',
 f'''# Day4 - 浏览器自动化爬取信息

> 前面课程对 Skill 有了比较详细的了解。这节课重点讲一个比较复杂的工作流，逐个拆解浏览器自动化在 Agent 中如何使用。

## 本课内容

- 浏览器自动化可以大大节省工作时间、提升工作效率
- 在 Agent 设计中，浏览器自动化是不可跳过的一环
- 拆解一个复杂的红人（KOL）开发工作流

## 作业要求

跑完整个工作流程后，在飞书表格里完整拿到红人信息，**截图提交**。

{VIDEO}

## 课后

按顺序学习，并在群里完成作业并打卡。'''),

# ---------------- Day5 ----------------
('day5.html', 'Day 5 - AI 工作流底层逻辑和全自动建站',
 '不写代码，5 分钟做出并发布一个英文网站。',
 f'''# Day 5 - AI 工作流底层逻辑和全自动建站

> 前几天的学习里，你已经让 Claude Code 跑了起来，学会了用插件抓取数据、对接飞书。今天把零散操作串联起来，建立自动化的全局观。

## 本课内容

- 搞懂大模型和各种软件沟通的基本原理
- 实战：**不写任何代码**，用大白话跟 AI 沟通，5 分钟内做出一套精美的多网页英文官方网站
- 直接免费发布到互联网，让全世界都能通过网址访问

{VIDEO}

## 课后

按顺序学习，并在群里完成作业并打卡。'''),

# ---------------- Day6 ----------------
('day6.html', 'Day 6: 内容机器 - 社媒矩阵与 SEO 爆款文章 SOP',
 '两种实用的内容生产套路，解决写文案的难题。',
 f'''# Day 6: 内容机器 - 社媒矩阵与 SEO 爆款文章 SOP

> 有了网站这个"基地"，接下来最重要的事情就是源源不断给网站带去流量。这节课把目光聚焦在"内容创作"上。

## 本课内容

- **套路一**：让 AI 学习行业高手的爆款文案风格，快速写出领英和推特文案，拒绝生硬的机器翻译感
- **套路二**：更厉害的「5 步写文章大法」——AI 自己去谷歌搜集对手写了什么，找出盲点，补充最新最全的行业信息，写出一篇有深度、容易被谷歌收录的高质量文章

## 附赠

Autoblog 自动写 SEO 文章工作流的 demo 项目，供大家研究：

- {link('⬇️ autoblog_v3_demo.zip', 'YWEwZTM1MmE0ZThiNzgyYWRmZGIzMzU1NjcyOTcxYmVfYWVhYzUxZDkxNWQ3ODE2NTdiOGRmMjllOTFiMWVmNjZfSUQ6NzY2MDA5MzEzMjY1OTI2NDczNV8xNzg3OTAxNzE5OjE3ODc5MDUzMTlfVjM')}

**安装咒语**：把这个文件直接拖到 Claude Code 的对话框里，然后说"请帮我安装这个 SEO 自动写文章的工作流，包括其中的 skill。如果在安装时需要提供任何信息，请告诉我，我会向你提供。"

{VIDEO}

## 课后

按顺序学习，并在群里完成作业并打卡。'''),

# ---------------- Day7 ----------------
('day7.html', 'Day 7: 终极接管与无人值守运营',
 '终极一课：实现真正的"双手离开键盘"。',
 f'''# Day 7: 终极接管与无人值守运营

> 训练营的终极一课！把前面所有零散操作全部自动化，实现真正的"双手离开键盘"，让电脑在后台替你默默工作。

## 本课内容

- **终极技能一**：让 AI 直接接管你的网站后台，自动检测、自动修改网页标题和描述
- **终极技能二**：利用独家赠送的 `tt-bridge` 浏览器插件，配合循环指令，让 AI 在社交媒体上自动寻找潜在客户、阅读真实评论、用真人语气点赞互动
- 亲手打造一个 7x24 小时不知疲倦、在后台默默为你引流的「数字分身」

## 附赠

课程中演示的**社媒养号工作流**（安装前提：先装 tt-bridge）：

- {link('⬇️ twitter-engage-pack.zip', 'Y2FkMTAxNWE4MGFkN2Y3MzdhZjQ0YWQzOWYzZDAyNWFfYTkwOTBhNTExY2UxODMxYjJhNzAzZWRkZGZjMTFkNTBfSUQ6NzY2MDA5MzMyNTkwMjc5Mzk3M18xNzg3OTAxNzE4OjE3ODc5MDUzMThfVjM')}

**安装咒语**：把这个文件下载之后，直接拖到 Claude Code 的对话中，然后说"请帮我安装这个工作流包括其中的 skill，并跑一次测试。"

{VIDEO}

## 课后

按顺序学习，并在群里完成作业并打卡。'''),
]

os.makedirs(BASE, exist_ok=True)
for fn, title, desc, md in pages:
    content = io.open(SRC, encoding='utf-8').read()
    content = content.replace(TITLE_OLD, '<title>%s</title>\n<meta name="description" content="%s">' % (title, desc))
    content = content.replace(COLOR_OLD, COLOR_NEW)
    content = content.replace(LOGO_OLD, LOGO_NEW)
    content = content.replace(FOOTER_OLD, FOOTER_NEW)
    start = content.index('<script type="text/markdown" id="mdContent">')
    end = content.index('</script>', start) + len('</script>')
    content = content[:start] + '<script type="text/markdown" id="mdContent">\n' + md.strip() + '\n</script>' + content[end:]
    io.open(os.path.join(BASE, fn), 'w', encoding='utf-8').write(content)
    print('生成', fn)
print('全部完成')
