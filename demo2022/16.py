def f(n):
    if n == 666:
        return 1010632056840781493390822708129876451757582398324145411340420807357413802103697022989202806801491012040989802203557527039339704057130729302834542423840165856428740661530297972410682828699397176884342513509493787480774903493389255262878341761883261899426484944657161693131380311117619573051526423320389641805410816067607893067483259816815364609828668662748110385603657973284604842078094141556427708745345100598829488472505949071967727270911965060885209294340665506480226426083357901503097781140832497013738079112777615719116203317542199999489227144752667085796752482688850461263732284539176142365823973696764537603278769322286708855475069835681643710846140569769330065775414413083501043659572299454446517242824002140555140464296291001901438414675730552964914569269734038500764140551143642836128613304734147348086095123859660926788460671181469216252213374650499557831741950594827147225699896414088694251261045196672567495532228826719381606116974003112642111561332573503212960729711781993903877416394381718464765527575014252129040283236963922624344456975024058167368431809068544577258472983979437818072648213608650098749369761056961203791265363665664696802245199962040041544438210327210476982203348458596093079296569561267409473914124132102055811493736199668788534872321705360511305248710796441479213354542583576076596250213454667968837996023273163069094700429467106663925419581193136339860545658673623955231932399404809404108767232000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    if n == 1500:
        return 48119977967797748601669900935813797818348080406726138081308559411630575189001095591292230585206733851868464009619343585194052091124618166270271481881393331431627962810299844149333789044689395510487167879769325303699470467829234399263326545652860748605075746366928323606645492277541120083438086727369377887676000211405318480244354207419604864176969950581435222198851194568984095705945549589054568321792338919149442985919957734792959402499096845643020401869381175603964424333222114125974374817804242633309769804293952870034619354125014210045647664063240162007560108665290568646128342557147350985358724154623253371867470765120422073867963935775258692109753041762094343569050497470353531764481503174750911858230906998361066084787758316110585736013365377431860738572261325738233656835271947352695180865573043834027955539012765489372645042504406597752357481931532872356635411224578334040522294746402829585458478708778346379431862368824819009177091444034885941394319343910223168655869761799669075059527608502465593181398566214786801211651657222004123456498258513120359126022843038535083709796101565934859483203933443308601475813108363074118562404412420191947127585482919172173045961122122701434297870691932154082986945954748251105782181586397275820342101470457300633590139512919549474113721711616912519714191760699935509810254849967087635936181176363954224186031346682928878492872249485456690138831610135377916327940503701400290125509132140782614640495733518048670983360134097860364762638658894873174499870133559364805443430831459505987809215393353387232078177562975021460595422358573128085417162336030235138652735438053034531962620811566019896879275257163988352090874930346115518331202927263708446729394381879888839549731876978682249320628599631628662375508826209854754631984276392670919216923002770077734756077549035942976209159416211581439461484509549370357486770276807687544580164314647595031368948490282897173328013518435758700056425922638411889496527975846052717958044813737086806600171993703579485864029383208714528950303253881360812631162134750100307772634337467012820470715650810714689905121432259528505483053930402217400686061612471659630192434864094539828085677465383026128353771071152304197549798870706139893609140045659756285435787771636258253666592102151236142132724425850991205720020493660580896600891888594659612927724357866265934517615841298789154462249169688860092640284756382431746120357767933119589280468687348061788072986362788582227019465263474828590646048451070702923434422714349595857654843699542321849363652767771978314681013589442955219879702008068934096624650625769705233333462826013860098698155180331145365652453482955497979915586438474687345677874451117702250441711504844638414485210092261397271970571029038581873069951161330495772310508760528249706514238384269808639507080418298318311361373628512041716415196868334254119137139589149597210032153545941114666530498906529240798164804007394775927836045668573993316428972539932745757171947402454257142633700815922407278403640595355142075599446056337986717212316223257763412164180899532722039383244462511410346646148863397237096276822656157561194665545757017429842404840309758925618650507921043007241637877939825811059339138925526124514467627126548126795078784022672860886251974581362141782786407402896309678008909663263987018538107050886193489012497405005820727271232733728141775132722013860591169620692789290456794698409808557447756701311883266010859016027592252397754508251628808293537776536569608111330584797160694847898923196743970244451842702266403326317319092117151143971679500042590269255093130215984418097418435474300467281949798227102529873732749027992079700287275900856241172902880909546551703263202853584498085358955307673717177961902081098618729046348849060249600000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    if n == 1:
        return 1
    if n > 1:
        return n * f(n-1)
print(f(2023)/f(2020))
