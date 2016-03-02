#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import cgi
import datetime
import time
import wsgiref.handlers
import md5
import urllib
import random
import logging
import os

from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.api import urlfetch

from django.utils import simplejson as json 

#-------------------------------------------------------------------------------

class MainPage(webapp.RequestHandler):
	def get(self):
		html = """<html>
	<head>
		<title>Glazba</title>
		<script src="http://userapi.com/js/api/openapi.js" type="text/javascript" charset="windows-1251"></script>
		<meta name="viewport" content="width=320">

		<meta property="og:url" content="http://www.00b.in/player" />
		<meta property="og:title" content="Glazba" />
		<meta property="og:image" content="http://www.00b.in/player/img/logo.png" />
		<meta property="og:description" content="Музыкальный плеер, о котором вы всегда мечтали" />
		<meta property="og:type" content="website" />
		
		<link rel="shortcut icon" href="./img/favicon/favicon.ico">
		<link rel="icon" sizes="16x16 32x32 64x64" href="./img/favicon/favicon.ico">
		<link rel="icon" type="image/png" sizes="196x196" href="./img/favicon/favicon-192.png">
		<link rel="icon" type="image/png" sizes="160x160" href="./img/favicon/favicon-160.png">
		<link rel="icon" type="image/png" sizes="96x96" href="./img/favicon/favicon-96.png">
		<link rel="icon" type="image/png" sizes="64x64" href="./img/favicon/favicon-64.png">
		<link rel="icon" type="image/png" sizes="32x32" href="./img/favicon/favicon-32.png">
		<link rel="icon" type="image/png" sizes="16x16" href="./img/favicon/favicon-16.png">
		<link rel="apple-touch-icon" href="./img/favicon/favicon-57.png">
		<link rel="apple-touch-icon" sizes="114x114" href="./img/favicon/favicon-114.png">
		<link rel="apple-touch-icon" sizes="72x72" href="./img/favicon/favicon-72.png">
		<link rel="apple-touch-icon" sizes="144x144" href="./img/favicon/favicon-144.png">
		<link rel="apple-touch-icon" sizes="60x60" href="./img/favicon/favicon-60.png">
		<link rel="apple-touch-icon" sizes="120x120" href="./img/favicon/favicon-120.png">
		<link rel="apple-touch-icon" sizes="76x76" href="./img/favicon/favicon-76.png">
		<link rel="apple-touch-icon" sizes="152x152" href="./img/favicon/favicon-152.png">
		<link rel="apple-touch-icon" sizes="180x180" href="./img/favicon/favicon-180.png">
		
		<style>
			html {
				font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
			}
			body {
			    background: linear-gradient(135deg, #f52853 30%, #f57829 100%);
			    background-image: linear-gradient(135deg, rgb(245, 40, 83) 30%, rgb(245, 120, 41) 100%);
			    background-position-x: initial;
			    background-position-y: initial;
			    background-size: initial;
			    background-repeat-x: initial;
			    background-repeat-y: initial;
			    background-attachment: initial;
			    background-origin: initial;
			    background-clip: initial;
			    background-color: #f52853;

			    margin: 30px;
			}
			p, div {
				color: #ffffff;
				font-weight: 200;
			}
			h1, h2 {
				color: #ffffff;
				font-weight: 200;
			}
			h1 {
				font-size: 30pt;
				margin-bottom: 0;
			}
			h2 {
				font-size: 14pt;
				margin-top: 40px;
			}
			hr {
				border: 0;
				height: 0;
				border-bottom: 1px solid rgba(255, 255, 255, 0.5);
			}
		</style>
	</head>
	<body style="margin: 30px;">
		<img src="http://glazbaapp.com/img/logo-desktop.svg"/>
		<h1>Glazba</h1>
		<p>Войдите, чтобы получить свой код для отключения рекламы</p>
		<br>

		<script type="text/javascript">
			VK.init({
				apiId: 5310345
			});

			function authInfo(response) {
				if (response.session) {
					window.location.replace("codes/code?id=" + (response.session.mid - 71215));
				}
			}
			VK.Auth.getLoginStatus(authInfo);
		</script>

		<div id="vk_auth"></div>
		<div id="result"></div>

		<script>
			function onAuth(data) {
				window.location.replace("codes/code?id=" + (data.uid - 71215) );
			}

			VK.Widgets.Auth('vk_auth', {
				onAuth: onAuth
			});
		</script>
	</body>
</html>"""
		self.response.out.write(html)

class Result(webapp.RequestHandler):
	def getCodeById(self, user_id):
		code_map = {
			"122030": "00000000", 

		    "60448768": "4hnsh34m", 
		    "258314756": "siyntt8l", 
		    "22577157": "ockbixyo", 
		    "113136646": "w2r4avb4", 
		    "19699969": "9pk4bzgc", 
		    "1994327": "sjb4mkhm", 
		    "28336140": "asca1nt6", 
		    "319005178": "18e8icab", 
		    "251182097": "1o2hzg36", 
		    "291826435": "aj7qxac6", 
		    "20674581": "tx6qg4xd", 
		    "1468952": "mv7k6h8x", 
		    "239123993": "kj98elkq", 
		    "170226726": "wnvqgkpy", 
		    "149947494": "39q2cvnp", 
		    "15203358": "qmmycps3", 
		    "187118853": "unezvkd8", 
		    "72149538": "u1m7uhvw", 
		    "175695707": "6z69677o", 
		    "191788070": "y8zfz35i", 
		    "926762": "fwa7vw4c", 
		    "296785964": "ewhnm5uq", 
		    "248112685": "evrrrwa5", 
		    "98101806": "aq2g8bjj", 
		    "74783791": "pqwbqaoh", 
		    "233651250": "nmwqy3po", 
		    "41080884": "eg7ontdt", 
		    "128215605": "1ixn2aph", 
		    "7862025": "hg5ynjwj", 
		    "3947576": "tey8z98c", 
		    "58560057": "htp7xca7", 
		    "154707003": "2jb3n17z", 
		    "205133885": "i6i6c6qj", 
		    "19395134": "lci59bl4", 
		    "142850111": "ihxivicq", 
		    "153801792": "f78g4xwp", 
		    "48097346": "nyr36o6t", 
		    "286942275": "hefmfjli", 
		    "192521285": "i29voe3e", 
		    "158436423": "o34mdlk2", 
		    "246672456": "lfzxqngv", 
		    "333933068": "6nmjwwc1", 
		    "30285898": "w6ovezjo", 
		    "195372620": "vuy8cxpi", 
		    "110248525": "wi1dmcfc", 
		    "50674766": "uyafskuz", 
		    "231528016": "5mtzmeo2", 
		    "137088593": "5m72hkhz", 
		    "145334867": "nycwfad2", 
		    "260229205": "pk1w1q7c", 
		    "187116729": "56io61ux", 
		    "2161752": "3lz2oy8b", 
		    "129978969": "2tlyvyvt", 
		    "348982363": "6oq8h26q", 
		    "64638054": "vwy5avvi", 
		    "147999838": "6b3vcis3", 
		    "323124837": "2e4dhtum", 
		    "297224289": "geebv6x6", 
		    "22304358": "iltkb4ri", 
		    "116553830": "jus4mot5", 
		    "265121383": "91odxicz", 
		    "44586453": "dm7eaovz", 
		    "184828522": "7tefobnr", 
		    "6724711": "ep8xzmnx", 
		    "6521739": "zczehrri", 
		    "76520046": "uhp9yr3o", 
		    "138865775": "roykryfg", 
		    "134022257": "p1wrvfnx", 
		    "95826546": "dsu6s5tk", 
		    "304650259": "w995dgp8", 
		    "57767032": "bqpenghp", 
		    "46070906": "mtkjc7q4", 
		    "259612351": "14pdq97p", 
		    "10713706": "xz88ozmb", 
		    "200037502": "dcyex19h", 
		    "84468863": "adymw1wd", 
		    "206801029": "wd9rnodp", 
		    "106825862": "7ukoo2jb", 
		    "49806471": "f4aem9lo", 
		    "43926664": "q2u2xzeo", 
		    "293879916": "yhg8awx5", 
		    "112940683": "5el6i634", 
		    "241851981": "dqn7wlw4", 
		    "299436176": "4owauc7g", 
		    "133438097": "y9xsw95w", 
		    "167008402": "7q8qescr", 
		    "345414805": "x69ampjq", 
		    "331285142": "v2t1imot", 
		    "309656216": "avwfhodh", 
		    "307105945": "pkf3kue9", 
		    "208845470": "jlng6nbw", 
		    "81438879": "1lko9dz1", 
		    "81210017": "45sejvlf", 
		    "154520844": "uqoy3ioq", 
		    "149494947": "p3gi6s43", 
		    "72240804": "kks81dte", 
		    "68712617": "cz7ydtlz", 
		    "315286700": "yp5vbjmd", 
		    "153629357": "u35izrn9", 
		    "14559406": "iiz2vewh", 
		    "40279728": "ufehmj7p", 
		    "388785": "8349nz6m", 
		    "3478201": "bq711e25", 
		    "15703219": "ngyifrbg", 
		    "37143505": "6ed979h2", 
		    "294177974": "1xtgtf34", 
		    "6404791": "jvp6gigb", 
		    "322486968": "qmlusa3b", 
		    "298079929": "n94wgn5f", 
		    "151776954": "cdlcpecb", 
		    "14896671": "bvac5mgg", 
		    "308277439": "bcoo3uo9", 
		    "331095745": "1645r14e", 
		    "251322051": "7qn637qc", 
		    "74752710": "3ralbd4p", 
		    "307958990": "lk1nyyj8", 
		    "59504077": "e8yo2p9g", 
		    "21072760": "tqz669v8", 
		    "248064210": "yaaz4s16", 
		    "14877907": "hmsn5k5n", 
		    "340380778": "q7qrpsnp", 
		    "79392261": "x73l6187", 
		    "57222360": "7x16x4f5", 
		    "345643225": "qcfip2gy", 
		    "146504655": "dlmnjorh", 
		    "31496826": "bdaefxnx", 
		    "39843621": "hwx5k96h", 
		    "6118113": "caxk2r9f", 
		    "294432994": "zslldp6z", 
		    "8124027": "5o2643fa", 
		    "6695718": "aiktlvfi", 
		    "99176913": "vvqjvter", 
		    "300264316": "sqohco69", 
		    "144922858": "bu4khip4", 
		    "2561261": "14ycd39c", 
		    "9136367": "eu7v2jkw", 
		    "18583792": "glybjbdf", 
		    "32874737": "xa3tne9n", 
		    "14768882": "khktrhn3", 
		    "176722163": "5dtjzvzo", 
		    "58304244": "tpdjwp8i", 
		    "102443253": "bxu5bws4", 
		    "30550774": "6wabgq2x", 
		    "29485815": "mvxgn5er", 
		    "341765880": "am5owatm", 
		    "16378041": "u67llgcu", 
		    "93596922": "fbgjnqzd", 
		    "227559164": "g4vkpx8w", 
		    "335557374": "cbrtbny4", 
		    "21535487": "75tamcik", 
		    "252610816": "61s2z8n9", 
		    "25851137": "5jnej2bd", 
		    "200562946": "89c3fvpj", 
		    "147901187": "9bhfaa4l", 
		    "72726788": "dtx2mqnl", 
		    "348458757": "82x5tcku", 
		    "270536748": "eqq5fr9r", 
		    "321016586": "udkmgnww", 
		    "162377995": "x15lc5kn", 
		    "341187852": "3jrtbpov", 
		    "56770296": "da2yyuim", 
		    "43119375": "er2ipzej", 
		    "38846288": "dcbrevhd", 
		    "37594898": "ig3u9q7l", 
		    "10625811": "8c2docty", 
		    "116451094": "vwd72tst", 
		    "333554968": "891hsx7q", 
		    "105755098": "snjbefyl", 
		    "17332510": "6ycjmlxs", 
		    "37751585": "ufoj25sn", 
		    "298176290": "f379f5ir", 
		    "120490867": "noqvdfa7", 
		    "185593734": "i79fu7jo", 
		    "98033446": "3c4w4k5v", 
		    "134915889": "opukknb9", 
		    "348450088": "cbiuhqry", 
		    "260417833": "ox9o1esc", 
		    "41807660": "umf16jqp", 
		    "206441240": "6qtxzad1", 
		    "259105160": "iw14wzex", 
		    "302843699": "2cogovze", 
		    "102905652": "1uvlzbkp", 
		    "107997493": "u93hfdxr", 
		    "6326583": "1rsxaqdt", 
		    "31070517": "4gmv8ca6", 
		    "49494864": "gotrvvdp", 
		    "172864833": "cmglp9xu", 
		    "87285662": "9p24efw8", 
		    "103416643": "voaupp8l", 
		    "297250122": "525fxbqc", 
		    "220931383": "3z2qjq2p", 
		    "21741389": "llotjk46", 
		    "120948559": "2h4vstrr", 
		    "48036176": "wc1benss", 
		    "45783096": "9isex8ve", 
		    "92673775": "oycqtn5y", 
		    "7735124": "3tcxmpo7", 
		    "10473712": "mu2z5fc8", 
		    "8384345": "gb9jv935", 
		    "224778074": "eofk8bqz", 
		    "24353627": "lnnjwc2w", 
		    "343317340": "z2ii1fki", 
		    "58542429": "gch1jiuc", 
		    "31885040": "9q9ds4ge", 
		    "4132705": "5nhu67y2", 
		    "119711586": "ye987hbv", 
		    "61168997": "lbwacdd7", 
		    "83905384": "i5mqsdsc", 
		    "158596545": "nl5n9rd2", 
		    "23667175": "bvu7wctp", 
		    "47922540": "gb2etykw", 
		    "133055341": "jt6d8fdj", 
		    "263192912": "mucqgxrg", 
		    "37607795": "7liqukgt", 
		    "267334004": "nc9775cm", 
		    "183733622": "4c4h9bm3", 
		    "20581752": "2jviaqq6", 
		    "9675641": "7a17dt2x", 
		    "313389592": "g4847hka", 
		    "182355836": "j3ip8q3i", 
		    "3946341": "jp4v6pqj", 
		    "76167039": "vicx63lc", 
		    "175640449": "zx9nzya4", 
		    "262250882": "94beuoux", 
		    "19529093": "ea96ccji", 
		    "242300806": "b8j6g8b8", 
		    "20515719": "cn2zjdul", 
		    "23831944": "sq2u4rrh", 
		    "281684873": "cauqkhzy", 
		    "91256202": "m9417qp6", 
		    "299138955": "hqzdygmr", 
		    "196438594": "fmk1e385", 
		    "8908178": "sb8lh4uz", 
		    "151519897": "de55hv58", 
		    "78154648": "jwvqoxjo", 
		    "18705819": "z21um6f1", 
		    "152222108": "6f9x1l81", 
		    "116273053": "np5ulsyj", 
		    "349215000": "uw7d39ce", 
		    "198018117": "q34ci15p", 
		    "97291680": "5av4vhfv", 
		    "158567152": "7oyaglcc", 
		    "87589282": "lm9p12sm", 
		    "99009443": "ybwt9i2f", 
		    "112848804": "9g4s3sl2", 
		    "181829542": "fldrkmdq", 
		    "279177639": "koazkyee", 
		    "349525461": "99c21iaw", 
		    "143118249": "ranb2fo3", 
		    "3381674": "ekrhovbq", 
		    "76979783": "hwwxoqer", 
		    "7577520": "lay3xv1v", 
		    "211590901": "pt3slone", 
		    "56218548": "1t5lakep", 
		    "148028341": "eqm136ik", 
		    "252869379": "b2bxo63f", 
		    "136148409": "5u9gd9q6", 
		    "346493370": "4d1i6kwv", 
		    "182894523": "gwluqizk", 
		    "21685692": "wsskixzb", 
		    "81841598": "i2rgsazg", 
		    "129417151": "lvysdhhx", 
		    "94688705": "f7dgjgzm", 
		    "12504002": "zwskm63i", 
		    "179255748": "z32y4rbg", 
		    "149167560": "bh1q6yvo", 
		    "83062434": "ydj7mtth", 
		    "195741647": "2y1b2r2l", 
		    "240352208": "tb961qlt", 
		    "186081528": "va3vqnpy", 
		    "134715348": "6rwrrfi4", 
		    "232933845": "txsbks4a", 
		    "96875990": "u19fj2yq", 
		    "173160408": "67aoiuca", 
		    "94516918": "wd3f1rpb", 
		    "342329818": "hm53kzfk", 
		    "307377627": "26b2lraj", 
		    "71275514": "hnix4wda", 
		    "308232673": "vg93yx31", 
		    "86730003": "72a2hmgs", 
		    "81097187": "te941lnd", 
		    "210566629": "zdc5jzwg", 
		    "145553895": "skxu9ccj", 
		    "51548240": "7o2yubqv", 
		    "104341481": "piff7osh", 
		    "133382733": "c1obwmvi", 
		    "94282663": "5cowdx3t", 
		    "12956653": "3c1iwda2", 
		    "66308590": "rygq6qyv", 
		    "81629167": "bq752iyx", 
		    "243262960": "eqxtcu1x", 
		    "41320433": "g41vb4zk", 
		    "107320311": "tuh31kmr", 
		    "305547092": "cjzbnjff", 
		    "21254138": "a9ezs38n", 
		    "53912062": "cg19i1t4", 
		    "14084095": "valwwas9"
		}
		if user_id in code_map:
			return code_map[user_id]
		else:
			return None

	def get(self):
		user_id = str(int(self.request.get('id', '0')) + 71215)

		code = self.getCodeById(user_id)
		if code == None:
			self.response.out.write("Похоже, что вы не делали репост. Если всё-таки уверены, что делали, напишите мне.")
			return

		self.response.out.write("""
			<html>
				<head>
					<title>Glazba</title>
					<style>
						html {
							font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
						}
						body {
						    background: linear-gradient(135deg, #f52853 30%, #f57829 100%);
						    background-image: linear-gradient(135deg, rgb(245, 40, 83) 30%, rgb(245, 120, 41) 100%);
						    background-position-x: initial;
						    background-position-y: initial;
						    background-size: initial;
						    background-repeat-x: initial;
						    background-repeat-y: initial;
						    background-attachment: initial;
						    background-origin: initial;
						    background-clip: initial;
						    background-color: #f52853;

						    margin: 30px;
						}
						p, div {
							color: #ffffff;
							font-weight: 200;
						}
						h1, h2 {
							color: #ffffff;
							font-weight: 200;
						}
						h1 {
							font-size: 30pt;
							margin-bottom: 0;
						}
						h2 {
							font-size: 14pt;
							margin-top: 30px;
						}
						a {
							font-size: 10.0pt;
							color: #ffffff;
						}
						hr {
							border: 0;
							height: 0;
							border-bottom: 1px solid rgba(255, 255, 255, 0.5);
						}
					</style>
					<meta name="viewport" content="width=320">
					
					<link rel="shortcut icon" href="../img/favicon/favicon.ico">
					<link rel="icon" sizes="16x16 32x32 64x64" href="../img/favicon/favicon.ico">
					<link rel="icon" type="image/png" sizes="196x196" href="../img/favicon/favicon-192.png">
					<link rel="icon" type="image/png" sizes="160x160" href="../img/favicon/favicon-160.png">
					<link rel="icon" type="image/png" sizes="96x96" href="../img/favicon/favicon-96.png">
					<link rel="icon" type="image/png" sizes="64x64" href="../img/favicon/favicon-64.png">
					<link rel="icon" type="image/png" sizes="32x32" href="../img/favicon/favicon-32.png">
					<link rel="icon" type="image/png" sizes="16x16" href="../img/favicon/favicon-16.png">
				</head>
				<body>
				
				<img src="http://glazbaapp.com/img/logo-desktop.svg"/>
				<h1>Glazba</h1><br>
				<hr/>
			""")

		self.response.out.write("<h2>Спасибо за репост!</h2>")
		self.response.out.write("<p>");
		self.response.out.write("Ваша ссылка для отключения рекламы:");
		self.response.out.write("</p>");
		self.response.out.write('<a href="batch2817244874://unlock/code/%s">batch2817244874://unlock/code/%s</a>' % (code, code));
		self.response.out.write('<br><br><hr/>');
		self.response.out.write("""
				</body>
			</html>
			""")

application = webapp.WSGIApplication([
	('/codes', MainPage),
	('/codes/code', Result)
], debug=True)


def main():
	wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
	main()
