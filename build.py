# Wraps src/app.html into a standalone installable page (index.html) for GitHub Pages.
body = open('src/app.html').read()
head = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#f6f1f2" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#161113" media="(prefers-color-scheme: dark)">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Shade Studio">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icons/icon-192.png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}[hidden]{display:none!important}img{max-width:100%}</style>
'''
title_end = body.index('<style>')
out = head + body[:title_end] + body[title_end:body.index('<div class="wrap">')] + '</head>\n<body>\n' + body[body.index('<div class="wrap">'):] + '\n</body>\n</html>\n'
open('index.html', 'w').write(out)
