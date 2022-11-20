import hashlib
import time

import requests
from urllib.parse import urlencode
from urllib.parse import quote


session = requests.Session()
session.headers.update({"Accept-Encoding": "gzip"})
session.headers.update({"Buvid": "XY30A9D303849C51D0D6F863F84A269E887E8"})
session.headers.update({"env": "prod"})
session.headers.update({"APP-KEY": "android"})
session.headers.update({"User-Agent": "Mozilla/5.0 BiliDroid/7.6.0 (bbcallen@gmail.com) os/android model/SM-G955N mobi_app/android build/7060200 channel/alifenfa innerVer/7060200 osVer/9 network/2"})
session.headers.update({"x-bili-trace-id": "e604d67d2efb03214bad66932a637983:4bad66932a637983:0:0"})
session.headers.update({"x-bili-aurora-eid": ""})
session.headers.update({"x-bili-mid": ""})
session.headers.update({"x-bili-aurora-zone": ""})
session.headers.update({"Content-Type": "application/x-www-form-urlencoded; charset=utf-8"})
session.headers.update({"Host": "passport.bilibili.com"})
session.headers.update({"Connection": "Keep-Alive"})

code = ""
tel = ""

data = {
    "appkey": "783bbb7264451d82",
    "bili_local_id": "4f8fa1cbb527cbbdc3f1f2af447279a720221113104854c6ee85433e906d6e10",
    "build": "7060200",
    "buvid": "XY30A9D303849C51D0D6F863F84A269E887E8",
    "c_locale": "zh_CN",
    "captcha_key": "68ef79b8b775bc3efb329b14f5875841",
    "channel": "alifenfa",
    "cid": "86",
    "code": code,
    "device": "phone",
    "device_id": "4f8fa1cbb527cbbdc3f1f2af447279a720221113104854c6ee85433e906d6e10",
    "device_meta": "53DBBEB6F74676D85479BBEE9433DB955925F22FFE3BA55D5F3E37B621A366AD023128E71EB950B0996AF1198BA2B9E0DE6A70499AF154EBB503D0AD3C858CBAD1F6C59396A466793675BFC229A789D45F5D0FEADD886F2057BF57423CEFEACD4263358677B94FB5758DBE23B25567B5D853110A2A40CBA0842B716553716A364D403036B796DFEE886DC5A5AD1813706229C8CCEAB0F36DFDE206666F81BA5A2C8A00F3E9AC2224FE5EFA5C62836DFCDF388980A84DBDC06547C216D80A9A866A3AE2608AE3942059FFC0F910DB9F071A0CDDFAC41F7E16799EFFABF3B0AE35B5D9D64FAD99C119E3F677D8C434A11079F4970633E47AAF94EFBF56859F14DBF47E828555C9F73F054E941D1878472206FF224081CA575D1CF4FB44718F0617A2320EDA2F3A1C82F62BD2FBD0EAEBD5E1C431F3C1080457F2C95A9A2957E8C22FB0861D1743F6F54022152F08C94E1677A8A58B2E7F43E438344AD785E07032CE57277CB7662EFF01CD747F9F9B475FB787ECC388425369725B54633FD9B310AD634B2671AAB3A2121E3C0C9CD23483B886649226C2ACE43BBB359840599C0AD51963F5BED3538895CB7CC910A82E3D2441FE4D417373F90849F5CD5601D058184CA9BF25287D71233EBDF76DA4AF39BA2FC78093F31470D316A446C59B97D354D1AF5F044CC8FEAAD8F10650D807AB73C10FB9BA7EB2E05D757BD2A6238616E0D42AD3D5AF4665D3219A1218151243FB795630AF0B5E9C91BD0B86A56ACB57DFC31ADF6CF3841CEF64E12EC18C205054A392A08D1DF62B8EBA259FDCA39277D70B2AC12D641F4D424B9260C320D54F93A317FC633E9BD760A64FDBEFF4536CE48F5299D7D9E57C18AB2D2D70FC72751F2428251B4034FCC92BD52DCDD491889D4E11E2F4534A5F75F5D1D4C20784495342E9C0CA6EDF8639B065AE0A932D2D939B56CE47D43D18A475B3924A2D827B166A77388529EED18E92C550AA3D1141492F20CB0AE55074C96FB13E1866D3D33D6082D4701B9C86D1A0886DAC9B928F66C4AB2869B378B55F16FAAD913685DDDC62357C4AEE771B618E7CB067A3AF2C197289EB90DEFFE007AA081DD9293CFC199A39542E6B7E1A43513BC4EA7DB17366BA45B81BA0D85944FCEF27F10D3DA56E5E0877E3A128071C508BFB05882C504AB6436AD752CBDA2F8E67CC222170DC7635984EB58B47F22222EF63310E93FF57D70A1FAA50135D80093886B92BF2D4759B26A7A1D862E9FB70CBD0D283D5E71D01C6C9861EA3FE39B29F23AC85650FD92DB1ABFD39236057291A4731AFA94A515E5ABEFBE6533E3E61D642C89DCFEDF81512E2DCA29FFB3FF817D42EFA9328A5188334679A22030A96623EF16E9BED79B1BA5A9E46128FD8F5F846363CBBF591629A63347A5983DB5104E686224421905563274279EFCF65B25B9F8249AEF45E915E8F4A906BFCC66BE47DB3A23D9B8719830F5C94D188DDE2BC625225B08DE1A425C0043CB04262F0411E539D21E4D719EBC79C8EA52D69B2D0FD9149C358BF20272513E23C67BBF59D4C39CBEFE38406EDFEC8193C8B9749B8FBE1468F4ADC0C15E3BDA1AFFC7141CB4322351A607E0E412AF985A5B9F6B35C60345A99C3662B512C4B1BA78AB35EB56C3E60BFD8CD6559A32B1E9F60BA3FCFEDFD75CBB6754A3D41ED7FD80A2880CEF9A5B9ECE4A63ABA0FF773EEA960B6508080627005AFEBF3904E2D4595607D4EEAB01269740A26300AB0E390993426BB6B14E384E298068D98A86DFA9B589F337DD5A6CA3CF426556E5D12DBB9B081E46D7C0B755579CE1D125CC15189056683E3F91B622BDB901F648308FC0BD73424D26B336A463FD07F6CBD877098B6A179DECD9F3E473204AB975C44B19E3F46BB28BD21A9D4CF4917A06E66AC9031E6270AD8D971DFA4BA454C4C0F215110A8BA7E62576AFAFF54F3F566818BC58312DFC84F6A3C63D549A18EFF04BEE02D521B2EF6E838D00B4F6796F22B4BB209B446F5A353EB025B0B1DE138D7376794E1431A20808D7E58C93A416BD00BBC5F0582628812726D127EF45212E5819671D28AE7241C5161357DA732476A0DF95F1E97F4666F2F93D186FBAEDE27F785F8749C21DDF8AFEB584DC25C9BA082898E6DB1739D388BC90FAA6F01464B14F1625C0431CAD6515C12DC67B41D15AD00D3E81DB10DE30A3646790D2060424F59B6AE46842D69ED077EB48812419D267E37540254631EB0C8382ED46728DC772C92E12AD2E9551FDF89C7D2DE026676FFD1EDCB01E6E3BBD0F9FE2B8DF56EE2E7755BFB3BB77B90756D933507F336F0053B3FE2F2418C8102B6EA0A25F992BF85EE0D6DB1D1DBDF678A1FB57157436B43AEA990D8405F296ACFB285CC766162ADDE0B186C8F0B9286A00D73AE3B964846E2A64B53495D9B54AEE2AAB190C98AE2F902097678F0EA127937732A2EFB5CF6252F87F65DA65F260D56F0F18101404700D1D720E9DF4226C2F25B8533CB66A37F73CF353E845CC59483D8EEF06374C5A5572AD8534AFADB6F2EF2A2174521B36225ED35DB4353C7B95A14BB5C6BAFA39BC1CBE81FB8CB6F858F59CBAE525937E8762B790809267334B1E00C582B046B3D96E003C03A72C753D4A2A6BBF764C4FDFDCF7D22DC954168786E822E03E1FB4DEAC14DF6527E67BB3039C532005FFFD1DE0006612ACA4AA4D3E4B94E6560F07D1F018C4E0DCF134E9F503C9AE3823CA76E2772F9A2282AE75A04D7FE9AEA6BEB121B25BD89CC5C2E5579D98E632F7592B4ADB5ACD8F4F727B3D67FC57AA95215C40510B6508FE576F70C3EC7D061CCB5DCC35370A0409C2BF06FF0D3D596B5FD128E527AA19EC07E9F0443C028B5754B424EEEBF0EAB03C01BC722427575BBC55CE44A4469D3E6555EE46A490089398731EC93AECDC7A30091CA16F913D96C276B2E10FC253BEBFA44CC1772E7B1C56A4DAFEA5FCAEB8B9BCBFE0DF4F5D378CA04ACA6AC2EFDB4F8673AA638E6EC99726EBEA2ACC912F4A2436F85CEEE49927891515C6FA1CE605611896AF9E7E17FE3F882C28E3E38128720D81DCC74229ABD44DC51E418E0424B10E67B04E6D483D39933C7DD46DC44F893EE4A1A971B375C45501C32C77DC7A43C65E74A989D30A64875A82A3E24E89A21CEDDD2F89170DA15539541C16D663DE083E14673A7015BF9A49CCF6E04F2DC7F9CC41634BC006A7CEC3E2E5B61AC250AD24933D9C7A3A90CC1E36B7A719EB096EFCC501BEE513904EF7D63EEBF98A3926FB2A2E15564F88D5F5FC6D9B895F8CDC800C5A8822DEA9F19786C34CC7A676B6DA15A10BE5CA90349370BF339E4362C4DF36C7BBD821D73FE128383184EAEF9FD3D6260D9288AD06F4BE2C5D1C0C9558DBE31A2E43B6E906A30130D4D4DD841A71B0BA3305907C18931DE3664EFE31D2442478DB132B0E19451970CAB4A1671643E981EDCE9D071D9EEB13C91F009A515FB4DADBB340A3C33902664610297A954392C919BFEABC62D2892BCFA08AF99D3983296AD111D4E012C0E76FAE4372E32B89B26F9B80F5E32590ACDA5CE27D7C35666DA17FF3A83B21C58B6EC19EFA8F215DA7C273FC76478DDC06B6110D3ACA7789A653F538C7EBC4C04EC682299465F320E878EC77E5538BC9F088A60D76C1FF1102BEDAD1B0A5B305D0C153FEF2230DD530674A92B83A60D700E807D36EEA6F0F59DCB0FB8F723EAC9B003F50C10CFB3F8D785D38C7E1892D4AF2810786702740F5B3A7E84CAA2579FAA4F8A8C02E77540347DBC6458899B3B778365DEC03D01214894415BA827337EB95352CA8AA156868F736EB8EE0B014E29386F680A8176CEF7FBEA462DB9E19FE4572211FEF4154B0527F805ABF966474DF8E494EF766E97F690CF396B40794DAB47495481CE41C2A8EEF10EEDED1091ECC04A05B69305F9B028801C2E90D980E2910D464A8DDBC2A02C6AE67241A19D8ED1230D24CA9071552AC9BE52C0D33F04161DFA12AEAAB41D74B5CE1FA3719B11951D94B227A307D17E9950A2F4DB39CB35225698A612985DCCF1492343C28E4C3B91C5CD2EF3860FD00B5F144C388AB4A37D075B68E44100FA25FA15670BCC31FECCD6DA457186876D65493642AA5059B4F5F51E83AA3945C2057F728CF5AE1FEE1EFB8E57495F376F53AF740EC3F718F609DB23A2AED933A2E3F60610B3C84C44E1BD5402A03AD3EC9B87C97D2DEE995F84CBCB72CAD16DD6E5A5797DF409AC56F9C9DFC74B19D641A724FAB933059D3AD27F6EDF874A6F75382BE9F718BF60703AEEABA71A5ED0F9C10042EAFC010EE6F7012A0831BE95C1F8B4C33F69C9E97059A719ACAD3C93BECF3A07420D6F5085218C7EC1DB342E91EB3BDC537913C1A610D7E117E1CB488466C0309846A8F3E34BDE10E902CA80DB3AD87F14B1844DE97CA486D5A87AD3404811FDE1E8480EF04F39510D0BAC7A418862425631DD4F52B0076219D255E13EDA1480150D0F9178FD6C89F42B6438AFEFBA9BD52E2F8BADB7BDD78AF41841A07AA85D8B5029DC2949E7660F81861C5F64E13EE7AA4022D63E59E976ED0E58302B092DC9AC6A7A1A3EECFA2156C62ADBC7FF05E8CB75144DC229C06E7388BE57D20C029530C6DA96A998BDA29977628E9DB941DD88231A4E03BF887B5F31A47CB03B6C33170DFED3341386D2ECB10B2EE926714E3D49DEDF9E5C4551E48315741E72EB3CD2F5CD8504B730711B2C80AB5A3BA15E46F7067BA52A9AB5679446C99C9F5763961518534429943B71146F14A1D85408163E82DE504C87C2C35B88AFC7C8128D79A644CF1B5DC7A30584B58F2A8CDD29C93B9184F2D8039E0AE00FF0166F6525238C6A333F660A4F956E178EB58572CA0878EBE55A63B293D490DC6A375AC3478B18DD957CC8C43C0E2F4B495CBDBB115BDD514EEDCC2C613F6C99128F7CB137AE97A02574C30E21FE10BC267DC078CF6988AF1807EA64B146C52D578FFC7897519BC0F1365011BDC33C358480E6D4D9451C21A047759A6E1700B7C487E0E3113F56881B11F3B73FC7FA1406CCF8B189CF4D63128F76A51692768D0E1D2C852647D8C61D99B311A11CD8ABDF3577E48726F2E72493E9796DB0A6DEA7B621D3021740F9CAF9A266EAB967850D393A34EBC023EF982AB22616C68E077B478E8E60F8BA2F8352F8758039DA5EDED2EC6E0DE0B67903CA3CEBD6D79ACFDEAED5865256BB052C81E46BF0B13D8BD9EBA5FC978F46014607C6B9BE0CA70CF4F890AF7C5A65D1ADDD4A71AF6088B5BD4CDBD28E27BE2D82ACFAFEB843D8C5B66004FAD53FDEA6679516E790BBE02FFA670679AE46D142F47FDFE816BBA5E36FDCBE04AA7E69A2E5A1CF7D77911EC04BF0203C99A18B70212C30EF712EE0236FEEC94A14FB339DB7608C63014581BAFB822E305B87837FF361F1BCFE2F789C6E8B10F4F8835526AA34BB5C0924D9F81273EB290233761394FA6F9C551B8E073C848FCCEB091F31A43A88CD42DFA5D545F932BFE3E6D13CFDE19E2BC794E31A326E2B01D223A623CBCD430C81A9A327537BF9B00FEBE9D74E83F246DAB2283B07A750A411831E594C98893C139CF92393423B100CFBFB1108DC7A8BC601BC32E288789A5CBFDAD3E542FDDCAE00E82E8997BEB4CD16F1269FD810675ADDE8BACB1FB44C391636728DE85C31CC40E0A861735411A73200576F5B72A4FC6EF4EF659AD7C8E28DDAF00DA3654175FE9A9014E69BFC445483E0B5D57217F4895369FC29AE141CD7E63F42A11EA76DB052E06C8CE5362560FF6F6F7FA0EB0665D06F96B9E7483A503B54C49E6D87627FDFB976A0B07923F44AC668A2BD7DBB7A03E428A7FBBD90A0A589CBF8110A00A10D369D8719E00C31606AB511966C202761C95FA97174B398705754C63A94F9404324796442AD0AC48DF4276E5C3E37EFD04B4E5D222485B6450D15BF82F41589451BE631EC821567DB8FA328F48583DCA5E37007402D820BEFFC8EE7B80F87226C1A0226A1C7EC3498B68BD8DD18E909340E5E3E64E3BFC352404750F4B7EAB26DC9B261F6E8A4EFAE5681FB195E218C66B6B848DE875DF554288C97C75AB9681768B9675C595BF531583D24B60846E2493AF51F57BA04753CBEF03B21E272747A13BCAC30DAFEBBF985ED03B6F9092ACC6AD3A6C86F54CA017FCA7CC695095C75BF0BE4007AC89DFC1940F125817D47E4F7F86A2669719A748DB07A1E09AFBEEE289265BAE981109EB3466705889B1A2F20F3B30A6FC4E683F24AAF4DAA5DAB942C4B5358A2D1D82669C9817E2C98AE744AE3A7EDB3DB8E913CF4C8CFD5C57DA771914708D47A018025BE9B34CACC9D6056085108D193D6F18C170E3873D21C1B96CBEC4E9D94C86C9BC76E0C8EABD04B2B0396829397DD2F6A67E25E91E1ABF5F921755DF2C905EDDB57A236727DA345640C0B70A218DD46DDC1E5808A5E9A87295D9481F3291A24009258E1CE5C311FD25F432F995FE8AEB785B8313E003DC350CECCDAA79721F78454E8AD025A56BF86C97B07D8251D4DF3BFA04AB4A5ABE1E121CD7D4A0E45BE3F84CCB34D3D723D0D997E8F7B08417A3C70FA02081BB7063822FD33C24CC16C994256166CAF90618AF7F3099F558111F5923527C6430A74DDA1DEB666FF05D35E63577AE5236C9B027CB10AB2E940CC5B1E32F3DB0EECF87F61E013CCAAC52F2182DA58A6E43236E876E44EA2E030DE36DD6CC18911590602A81A749E1B9AA7D1207D7987AB2A3423F02E9969E1F99BCD3DA54FD04893FF1BDC1FBB8379EA59FB882BEF71736122C412B431E9FC623B21F04A9EB1D8D036138DD1EA2C6CA253BE396D7D6907C0D6E80F1BF65F3FEDEEE6E28F878DE0B9ECA886E24D842C6ECB1A2D49662E692D8518449D2ECA7A0F76E0DC59A38D82ED016D417C635D1BE93F0FB761BE999DFE8BE1061B17706C945B3EC4B796192530EA40165B62ADE4A9AA26FEA14A87AC31B222CF651BA9D3051602E44E43E0C94998FF238BBD2E0133F6B285014182388DCC8D0A2A3E2D083307F5849C1D5F76F65F16325875FBED1CC152859D0EA152B9EA7AFBB21659E9B1AC28B455D6A7A3922645BE7331F3AB562FCCC2F7733ACEACCC73BE4B8CA1E7DF5776AD107CA6D9D8928D04162C87AB3B7943AD8E1F6182E777FEE3D767E3AE34D4B6CEF09B0EFFC74FCDB0B8C502065A30ABDCE808D89C8B08C16B49AD24484C13964EBC01F4C901CBCBD2BAA87C9DA3403A27676A31D9E30209687E5D6311C149B0153D988B7B8EFE628CF512A604E535A58D39F5977D7ADB612B6BF9DFB4D108CA1E2794EE486015694444EFF31C9B99D8AA8EBD2052F8C371979BBC54B31F84D82E14DB93567FB8188E7500577500CC13139961794E72A19C80E83EE6F3767C3A695014F8509FB971588060C01F52E1C7EC32E648CE2B1CFDE48FF60FB1673421364E5A5F33BDE5A824A9267E534DD4D308C75B59E23D053850BC9B7F681414A6B653E437F2F59A45C14A65B9E489CBCA67D8D07BEF98718AC6F3889B4BC17EE130447637C31F5D63761E0BC235338D8EBDE9E2D54AB4D50ECA889E87C764491AF56933BFC34267DEF0B4F7BB1D105AD084973A1E563D116E4D322F30E7236A2F95467AFDCBD551F4E8245D85515B619D4BD2A97A9EFF3085BC5C07DA4AE29BB354FD4B0FFA0ABEB293095D4D2BF498370520BF327B74B15652E1227DB937D4E457F361F9EE2744950DDCC7F5AF6E91BA2AAAFA9B000DCBEB555E7EF36EAF368C535EC45BFA16DDEC52CB413B1ED02E49AB31865A83985D459A28029FBE341EE128956CB0B42262A2B1C78B32F950331A16E49BF6FE3620BE8686CCDACB934281A76BBD56FD289E2B438866D6A3DC17E749E227384E119C2F2AD05EB67947A60A5DA396C1F2F730A457CF99C3411DA27F33780AF11CDD50232BF0411F388094530AE5536247E4AFE00107A4CA289D48BA7A3D91ACB2978EFCA67B6DB03372BA37C8E02C50E6E96DC59BA19BD1BFC66AE23D9F1C75FE02EE57D9EFB437B360F9DDF665026A98EE92E893F080B2540BF3F143A3A5E1A02EA0B454342A8914A85203EA6805A671C3D6E1F40E0864F7844C3BE16C50DAD94E4A89EBA8B9493A729199B97B7E8DEB0A6C3090DF76E806C30B34187C5F9A88B45D2DD5DB36AB6C87BD046975054541C2BDA488F6A0D7EA3F30CD8582657196670E458DE1639018921A9FDAFF706B5639B8ABD08713ED7443318C5C2A0CC49D48BB425099483808141290BE5703E9953A15B432CE0283963B0D9C5244F1B2FB10F9E4264386CFED277E31ACC824D49C41188B6AE5CAC2A877F3327A86D410C41C03FDD65514F4EB961BCFE12B30ABF448CEC4F317D3662D7E601FC270C8FD7C35211707E7F5C3B879328FF4BD4FB0B1B1BFB2CD953E198DA3DCABACB75CD2F85B72E1D2E2FBC4DFDE009FAF5FBAF73B30A5DD26F9908E86A24B94625BE48F87AC653520A8E58DEA0184D363ADA23B7441E418DBAD717AA8A5517F4DF9966658B0FEB1166B166B859AED36CC578A3A08D7E8669AA4F831613C040F44F29F0935D71A7A2E034BF53F1BFFA2A1FC12223CA70BE5AF99CA06A7473AE79B6E7BA53F2A5B949A709B1B7678BD754CBA2199F9CADF609BA43F6BF71D5860DAFE6D6700F92E5CBDF3006372167E9A25C23F06EA50EC7BD0448021354DD89675297038DEDCE5B2568FD9D06C383AC397BA30C28981E5EEEEC7E7EA8F45D1C646E87EA714869C814D0109927D7233B9920727FEC55025DBB9BDCBF3CCCB23FDE7B8134F0C3DF84125957BAE94FFE0035FB8842A7C73931E526459320B4A5A6CDDC7EB15FA1703861F01FF934547EC19608C79CD6C621FB1A72225DBEE24309D22EACD6B44DF8C80FED95928010BEF9672ACA9E299FB27E92A003E65EBE5C621C9C8B96507E7A1A405F44560C01D8C8F9473D6BDC9EA9FF4D9FC9B8B6DEFF4F2A731A670A938FA626DFFCE35286CAC6BB0C6A55609AE44AE39697E74894D24AE3933C7BD18918A415862BAAE97209A08EC34C9BF403951C040459B15D1C181C882A98477112D21A41BB70C57763154FB49446DB95FE720D149C66A896ADA7CAD9E01BCF76EDD5B77769C95FA78E9354455D674DCACA3189DAD0DB9FE41B49F616936C4B24C8984947184DE7DA62F900A4C75C97B4D8EB5E9B91B6BA649ECBD8179668B0E6E4B478783E4146661B9204C2CE70E2CDCCBC19071494719D4BA86C2BDBF16C5B84D3CE2D1189863E7933AD7CBC6864CF509095BB0D7F70CFC236420CB4F8D291B973EF965BD3A4C21B7D922FF194D676BFC44B92BACEFE0F20485DC0B118B53F0A09E5466B3F601023E46609A3106C688401D4A8ABE06FDAC65F2D39974F7B6FD9770CB170543F0820BAA15268B5CF3CF077550AFCDABA7F0D13A504917E6CB4A9CC9D23AEF3458CD6C3A31E332ABDDC21DC41DEBBC3A71EFA64C7A9C15BBADFACC49AFCB9F3EA657CC2D323EE4CDE665869DC5B4D7C1D9AD702A6550064FB9FDC411E871BC1224AA6B4161FC73818C440EC0FAFAEA45F5878FA3B93BC71D97F96C6A879101401538310D105830A925347D2F7357F9B25428101B48B21D7C282C15307F1F973179A07D1A0825C42969732FAEE84E0C8682E018FD34AF56C1699E0390770C115FE841CA6D6E1D02EFF87EDB97A94499F68D0CE56EB2BCEAC28B7953A1D648B2ACC66A2A3D6782FCBC17A499757E642203D59D72F0BCCF8CFB24B6C1E75372684C6B94698C83540B704ADD18717E8A05D0231BEE9164C382877E0E364939E741D765DB5367C2ABDB7B3C8AB52AA6276553410683CF77B2D5442A9C09B9AFD6DEDD53A20DBA8DC77F90708BD9ABE7E3C19DF6E4ED0E41A8EE4EB48534D877E071D11D414D56FFA02F89C78333866589912E16B651EED55A672E1E2367A326D6D78E1D5DBA70F9F43763886B5D32D5BD81AE8696955698DBFCEC8D56A8B2405107BC0957D016F7E8B491D7D0A820C770B2F96213E3B0AC3F35F4C82D6BBBDD2CD4672B43B6827C30A5ED4F75E3E88C157920237D4A298A6F5A260E0547986FFD58A08B35F2AA044B5BB41B2FEDC0DF1F7CE159C7BCC2D55363E82C4731F00E5750E36A196FB48B31A9425289117EE221F7CAD266B6DF836E5231898A599173BACB35DE00929A97A3BC6D4CB2CF627E6CB79A651C7524FD58D4A3786C1E44A9D95E214D6716C0D5D84E15B63CDCAE35E3C1F65A788AB126B87E0F4D470FE8F32F85E2483B730B4E15255BC20B6BD9DFDB6930B36289F4E985F1B846A0C9628719B6D19800454A9868809D763A2996C4B26684BFA35F58548AA12497E68B1AC62A6C18903426E2126A743014DDBB161BE4DD368C03F76D5818A3B018D84201ED31CFDA08489743ABA8F72A6D4818C5895075A3BD2C8CE764CD7B38093216A34C29CD55D88972ADDFF1C556B64B264682BA4BD4FAC252EF13BFA33AF85706AB88B9C6D08749AC5137A23A762233857E6DA4F2C37D11A2A2FD62CCDD4F655BBD355D6C6CFAABFA1D86C45731052D162306C7F5C62A902D754C689DA0B2D9D707AB9903863EF093C66E2D8F1990C301B97CAF9FBF482A73FB95584B64368577AD00615DC90BF123892D55B3D1E22AFD24884ACE07E6330D93CD3AC4529443DC42C1114712CC5134F82E80F21BB9751A67242F935203635EC811C5D1DC9598BA5A7EC426C96F2C489016FFD2090FD54E5E78067205776079CE4942828B5BDCA5806CB65C79244FFCDC46613010B77CF47C31F0688B7430ACFC33B28E0B3153BEA0DBD8D24E47AA149F603296CA517B1A3554427D6E34CAE41B7BC13D2C5C6488E5F3740EF402DAF8CFF5E769972BBF6AFC654EAC4F54BF4467A133196EE8271FE2133D11A5D74A2E866F7AECFDE4A7A10AC843D8DADF5669E8308635332C5DBF4BC29ADBAC75406F586CB9BD5AE9FB12F9D79D9A22EAE47309DD2B97B7668DD921A1A17DF4B0CAEB1F2AC928D152663910A6DE2578596333F70D1C238231FE372C80BA5E148FEFDFB41B334A85CC68CA0F0E133C1578860477ECE92CB0BEB7749112A57A69A45113A875929B164D49BEE0AEA5D8302FABD226C70441735D5F0BBBF5162C5FC898FE368BBF8A65A82F53ED19ADD58C97033B638AFD974DFBB2B7BAC113AC807C343E4E705468500756D50BC8056E588C804EA4CDB097F0C56E5920347B7381E26366EEFA281A4729186A377D9E2DCBBC18DC867578B5353EF92CF3F1F8DE1E7A43E2305587CEF9F1E2C94B3958AD00192E37AD041EC03F2087AB326D3E52A23B8561D746A23EFF51077A95CF615D24B01B8EB388E80AC8C3E5C1396F86FBB39A2C6AC815FB4AFD4B0D8333D8A01D24F941E23D016FB3F20ECEDED1DBE19E849AA24AC65F05C71D40B0F0E31CEF754D435A41FD5DCF7E31D578E0B6516848725567721CC0FFA67E831ACF228DC99F4C925DD3AC2F5EE89662FC131E2722ADA8F5EE32004F21FF2BFA4E0560477A6977C405AA0E02F20F7F7945BD8E84518D720508701AD1C36CB5B7C1362F40CA5FF52113A2E61600AC2791FC938D166C6700A536274EDDACEFE2EC4D012C202129640D7C92F57315785A58CCA304094A27477A9F90405C33EEC4FBADA0BA158D973D2FA888B44D19714835DD64B6576783600E6976E513B9438605A48E1E39B3B753C1FC90CDBF90C325B51BCF45FE1FAFDBAB6D6B67A072076037EAC0C78DB9617D04F06020202814BD425DE487C46101FECA94EA9EFE284E70BE65439C83B469361FC688CF13C695829515F423FCE77845185242E62B1F8D1E2E7E5FAE91F782246C92B4C42A64DA4B0026079D59809A35D1BB6DEB8A4619B37E8BA7C69B96B8D48D434EA3ADB92C3E2870DFDF851DE948A28FF28CB676A3A2AAE6E2399F3C61E2CC26B451C35BBBD9C94F2458FB238F3C8BA732154668AF5FF05DA8197864E8FAF69FA0CE2CFCE024C7B38A0F7E8E3CE79524233AEA6D1D520EBF000DDC7CE67EE7F946206A541AA21598D3A1C23CCCAF0D7655B7182F0980EF4B9384A69DE0C78114CBBE4F397E3F13E9E31F99AF89BC1F0D8518885C8E22FCF3A8053F3BBC08297A40EB8930DE01861C65B89B2D3CC5E692441338535898D9E38DE0309B4B435DD0E8ABD50C036109A6836CA88906DE0725313D235DD4EFCB91F14F106F9873B49AAC7DE20B507584BA3A1871BE1AD4A9D996DAFF388815B96CD7294B201BD04BA5487D47610FA3E880058D2C33F14115A0100DB5C17AA9EC40C3DAECA3E6267246491FA231AF3327209082D79D6E6C971FBEB21E4B24D15BF96571367352CDEB82B958D8A8B10E944DC40BC1DF64F44358D7AE1C0EC28544CCDF64E0786786D560A2CC4DC47DF9E7B1AC877CD16468C9825B02E7A49BF2B6A876B1DF1E884CDCBB6435A1EDEA480FC171EE4134C4E16F87FEADD5B4C548D1811AB291F490F551AB690DF37C54439BE8CA5928909C6672F8951C154A0B6C7B2CA8AB92F4314A60669C93D5D28CA8E6EF9207B10C854850BBA3F2760282A55400D48DA10272C504622C7DEC5989E85A9FD907B8D3C03D132DBA58BE0112F450AC49B795E4C07D0DDBD7B90F59E8A1216129FF37CBDEED99A66D67E251B7E18BBF60FE71C54CF3CFD2E7558EF1BA1CA879B0D342B35300DDAADFC1464F758B5386246844487FA4E5FF7E2E1FA2039DA2AADB490B116DDE2ECC7F86EACCFDB4728F95772FC8A1452BFEBA7CB07359ABDF0D6B95641A2D9A1E24B9E50D33BE3569077E0156792B66EC2B82B8B331EA7C7A632DD4F9CB60563E55F58612C140FDA543D5AE16789BEAF9C80487C3A72D2EBDB5BF39BB0EC94783F0071523E6CFA6B95B0E9991D2BD06342DADDF2FD4B3F5DC17619B46838FB4C8CF72941621962BD63E881E41625E7A0BA1C496985BE802E3E63358CE2DF32E6F9AD56A966037BB4907ABF5F7BB9798892336696D0B71",
    "device_name": "samsungSM-G955N",
    "device_platform": "Android9samsungSM-G955N",
    "device_tourist_id": "20605230970864",
    "disable_rcmd": "0",
    "from_pv": "main.my-information.my-login.0.click",
    "from_url": "bilibili://user_center/mine",
    "local_id": "XY30A9D303849C51D0D6F863F84A269E887E8",
    "login_session_id": "e4413e7ce4d97ed505b30fb8d9ab6585",
    "mobi_app": "android",
    "platform": "android",
    "s_locale": "zh_CN",
    "spm_id":	"main.my-information.my-login.0",
    "statistics": quote('{"appId":1,"platform":3,"version":"7.6.0","abtest":""}'),
    "tel": tel
}

data.update({"ts": str(round(time.time()))})

ddd = urlencode(data)
md5_h = hashlib.md5()
md5_h.update((ddd + "2653583c8873dea268ab9386918b1d65").encode())
form_data = ddd + "&sign=" + md5_h.hexdigest()

res = session.post("https://passport.bilibili.com/x/passport-login/login/sms", data=form_data)
print(res.text)
