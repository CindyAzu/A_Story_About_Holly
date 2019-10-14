$ config.developer = True

 #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 #Custom Transitions
image alpha_control:
    "scenario/A story about holly/assets/spotlight.png"

    anchor (.5, .5)

    parallel:
        zoom 0
        linear .5 zoom .75
        pause 2
        linear 1.0 zoom 4.0

    parallel:
        xpos 0.0 ypos .6
        linear 1.5 xpos 1.0
        linear 1.0 xpos .5 ypos .2

    pause .5
    repeat

define alpha_transition = AlphaDissolve("alpha_control", delay=3.5)

define dream_transition = ImageDissolve("scenario/A story about holly/assets/imagedissolve dream.png", 2.0, 64)
define swirl_transition = ImageDissolve("scenario/A story about holly/assets/wipe15.png", 2.0, 64)
define checker_transition = ImageDissolve("scenario/A story about holly/assets/wipe12.png", 2.0, 64)

define dissolve_quick = Dissolve(0.3)


 #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

label scenario_a_story_about_holly:
    $ h_holly.name = "Holly"
    $ sandra.name = "Mom"
    $ cassie.name = "Cassie"
    $ scarlet.name = "Scarlet"
    $ h_kisaragi.name = "Blaire"
    $ temp_char = Character("Girl", kind=name_only)

    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    title "Session"
    scene bg corporate lobby small
    play music h_bgm_issues
    outfit h_holly casual
    show h_holly b_8 at centerleft
    show h_kisaragi a_3 at centerright

    h_kisaragi "Take another one Holly."
    think "I look up through a curtain of cyan blue hair to see my counselor, Blaire, holding out a sympathetic box of tissues."

    show h_holly b_7

    holly "Thanks.."
    "I sniff pulling one of the box and tucking my hair behind my ears."
    holly "I'm sorry, I don't mean to get like this every time I come here, but it's like, I'm fine... Then i walk through that door and the floodgates just opens."

    show h_kisaragi a_11
    
    h_kisaragi "There's nothing to be sorry about Holly."
    
    show h_kisaragi a_11
    
    h_kisaragi "And you're getting through less tissues in each session so we must be making some progress."
    "I laugh a little, wiping the tears from my cheeks."
    
    show h_holly a_9
    
    h_kisaragi "I want you to think of these sessions as a safe, judgment free place where you can just let go and let out what clearly needs to come out. "
    
    show h_holly a_13
    
    holly "..."
    h_kisaragi "Eight sessions is enough for it to be clear. You spend you much of your time suppressing emotions and hiding from the world, it's good to let it out sometimes."
    "My next sentence came out as a mumble"
    holly "It doesn't feel that good though.."
    h_kisaragi "Give it time"
    think "How can she smile so freely.."
    h_kisaragi "I promise you'll feel better soon."
    holly "I'll hold you to that."
    
    show h_holly a_14
    
    h_kisaragi "I can assume you'll be here next week?"
    "Throughout our conversation she'd been taking notes. scribbling away in her little notebook" 
    "My grin slips a little at the prospect of yet more talking about myself, but i assure her that I'll be here again next week."
    
    show h_kisaragi b_2
    
    h_kisaragi "And next time bring your own box of tissues, I'll be broke by the time you've recovered"
    holly "Yes Blaire"
    
    nvl clear
    nvl_narrator "We work through our deep breathing exercise, signaling the end of the hour is in sight and I use the silence to reflect. 
    She is right that I've cried less and less in each session, but I'm not actually all that sure we've made any real progress. It's been two months for Christ's sake. 
    Surely I shouldn't still be crying for more or less the whole hour after two fucking months?!"
    nvl_narrator "What frustrates me the most about these sessions is that we...or I, as the case may be...can't seem to pinpoint exactly how I got to feeling this way in the first place. 
    I work full time and am doing well in my part time degree, I can afford to pay my rent comfortably, 
    although we are getting a new house mate to ease some of the financial pressure. I live with my best friend Paul and his girlfriend Bethany, who I absolutely adore. 
    I feel so guilty that I want for nothing and yet here I am stuck in this downward spiral of despair and misery, while those a lot less fortunate than me just get on with things."
    
    stop music fadeout 2.0
    
    nvl_narrator "This train of thought carries me through the last few minutes, then out of the practice and into my car. 
    I sigh deeply as I pull my seat belt around me and click it into place, taking note of my tear stained cheeks, sore, wet, dull green eyes and cracked lips in the rear-view mirror. At least I don't have anyone to look pretty for back home."
    
    think "I suppose I have no choice but to believe Blaire really is telling the truth and one day I'll feel normal and happy again..."
    title "The day after..."
    
    scene bg connie kitchen day
    play music h_bgm_arms fadein 2.0
    show h_holly b_1 at centerleft
    
    paul "Holly..Holly..HOLLY! Are you even listening?"
    "I slowly push my thoughts away and turn to face Paul"
    
    show h_holly b_5
    show paul a_5 at centerright
    
    holly "Sorry Paul.. Did you say something?"
   
    show paul a_3
    
    paul "Christ sake Holly, did you get any sleep yesterday?"
    think "Sleep? When was the last time i got a proper night's sleep.. high-school? Yeah probably.."
    holly "Yeah I.. I slept really well"
    think "Fuck i know he wont believe that."
    paul "... Sure."
    paul "Anyway, I was asking you if you wanted to go for Mark party on Friday night, since your last exam is this afternoon?"
    holly "Ehm.. HMM"
    "I hesitate, I had planned on going straight to bed once my final exam was done with, the last thing i wanted to do was go to a party with Paul's football mates."
    "Not that i didn't like them, they were just a bit much when all they did was sleep, practice, eat, repeat."
    
    show paul a_0
    
    paul "You know Blaire would tell you it's good for you"
    
    show h_holly a_35
    holly "hmmmmmmm..."
    think "I know he's right, Blaire would tell me it'd be good for me. The theme of our sessions (despite me ending up an emotional wreck each time) seemed to be shifting towards me trying to get out more and be sociable."
    holly "Is Bethany going?"
    paul "She's not coming back until Sunday remember?"
    "Comeon Holly for fuck's sake! You're always saying you need to get out more..."
    paul "I heard Erin will be there"
    
    show paul a_1
    
    holly "Ok. First of all, you and I both know that it's you and Blaire who think I need to get out more, not me. Secondly, all i want to do is sleep, not go out and get shitfaced with Mark and CO."
    holly "And thirdly, the last thing that would make me want to go to this party is Erin fucking Dawson"
    paul "That's not what you said last time when she stuck her tongue down your throat."
    
    show paul a_7
    
    holly "That's because I couldn't speak!"
    "I threw my pen at him"
    paul "whatever help you sleep at night"
    "He laughs, running his fingers through his dark hair"
    paul "I know she got your panties wet."
    holly "That's fucking disgusting Paul.."
    
    show h_holly a_2
    
    holly "And I'd appreciate you keeping your thoughts out of my underwear thanks."
    #change this shitty dialoge later
    paul "Alright, alright, {q}chill sis{/q}. I just thought you could use some fun after all the sensible shit you've done this year. It can't be any fun working full time and studying for a degree.. Think about it at least."
    holly "Fine! I'll see how I feel on Friday once I'm done."
    #maybe animation here?
    "His face lights up Happily as he bounces out the door like a kid at Christmas"
    
    hide paul with easeoutright
    show h_holly a_15
    
    "I sigh loudly as the door closes behind him, I wish he'd stop trying to force Erin on me, I know he's only trying to help and he's been so supportive of me recently with the counseling and everything, but Erin is definitely the last thing I want right now."
    think "Don't get me wrong, in the conventional sense of the word she's absolutely stunning. Roughly 165cm tall, long luscious blond hair, bright blue eyes and a figure she clearly works hard on. But there's just something about her I don't like, I can't even explain what it is, she just puts me off somehow."
    "I sigh again..."
    think "Thank Christ next year I'll be done with studying. A quick glance at the clock tells me I've been back from my session for roughly three hours... And I've been reading the same page for the last hour and a half... I think perhaps I need a break."
    paul "Oh! By the way,"
    
    show paul a_1 at right
    
    "Paul sticks his head through the door."
    paul "I think I've found a solution to our roommate problem."
    "I was quick to retort."
    holly "if it's asking Erin to move in then you seriously need to re-evaluate that thought."
    "He wears a devious facial expression"
    paul "Jesus, don't worry so much, i wouldn't dare do that."
    "My eyes narrow and I raise another pen threateningly"
    
    show paul a_5
    
    paul "No."
    paul "It's my friend Haley, from UNI. I think you've met here before? Blond, about an inch taller than your.. Ex-Amy? {i}Anyway...{/i}"
    
    show paul a_6
    
    paul "She broke up with her boyfriend and needs a place to stay. I told her about our spare room and she's really keen. She's coming for a look on Saturday."
    holly "Have you mentioned this to Bethany?"
    "I asked this knowing all to well Paul had a habit of making decisions without mentioning it to anyone else."
    paul "Of course I have!"
    
    show h_holly a_11
    
    "I gave him my {q}I don't believe this one bit{/q} look."
    paul "She knows Holly, I swear."
    holly "Alright, I'll chill."
    
    show paul a_1
    
    paul "Awesome, she'll be here at 11"
    
    hide paul with easeoutright
    
    "In throw my pen onto the dinner table and lean back in my chair, cupping my hands around the back of my head."
    "I glanced at the appointment card I've placed on the table, I sigh again. Blaire would definitely be telling me I needed to go to this party on Friday night.. And who knows... Maybe I'll actually enjoy it once I get there."
    #--------------------------------------------------------------------------------------------------------------------------------
    title "Friday evening..."
    
    scene bg connie bedroom clean night
    outfit h_holly casualdark
    show h_holly a_0
    
    paul "Are you ready Holly?"
    
    play sound sfx_knock
    show h_holly a_4
    
    holly "Almost!"
    
    show h_holly a_0
    
    "I hadn't been home from my exam for two minutes before Paul started shouting at me to get ready for the party. I could sort of see where he was coming from, allowing me to get settled in the house would mean he had next to no chance of getting me out of it again."
    
    show h_holly a_2
    
    "But I really didn't appreciate being chauffeured from room to room and being told to get ready. It was like being in the military"
    
    show h_holly a_0
    
    "Paul also seemed particularly concerned that I get dress properly, pulling clothes out of my wardrobe and making suggestions that I put some make-up on, which was unusual. Normally he wouldn't have cared if I'd gone in a {q}onesie{/q} and slippers." 
    "As it was, i ended up wearing a cute blouse, where Paul insisted i used my most push-up bra possible. And the only pair of black jeans I owned that made my ass look nice."
    "I knew he was up to something, but I was so preoccupied with being shoved out of the house again at light speed, that I didn't have a chance to ask about it."
    #----------------------------------------------------------------------------------------------------------------------------------
    scene bg sayaka house dusk
    stop music fadeout 2.0
    show h_holly a_9 at left
    show paul a_1 at Position(xpos = (placement_of(h_holly).xpos + 0.10))
    show h_mark a_1 at centerright
    
    h_mark "Hey guys! Thanks for bringing this stuff"
    
    show paul a_7
    
    paul "No problem pal"
    "Paul slaps mark on the back with a good thud"
    h_mark "Hi Holly, you look great!"
    #move mark -> holly -> back
    "He kissed me on the cheek as a greeting"
    
    show h_holly a_25
    
    holly "Um, thanks Mark. Where do you want this stuff?"
    h_mark "In the kitchen would be awesome, cheers."
    
    scene black with fade
    play music h_bgm_dolphin fadein 2.0
    scene bg sayaka kitchen dusk
    
    "I wander through to the kitchen and deposit my bags on the table, already wishing that Bethany was here to keep me company."
    
    show h_holly a_0 at center
    
    temp_char "You came!"
    "A female voice suddenly yells from behind me, making me jump and almost drop the bottles I'm holding."
    
    outfit h_erin summer
    show h_erin a_4 at right
    
    "I spin around just in time to register to my dismay, it's Erin and not Bethany, before she wraps her arms around me and kisses me full on the mouth."
    h_erin "You look gorgeous!"
    "Paul's concern over what I was wearing becomes painfully apparent as she pulls away and looks me up and down, her eyes lingering on my chest."
    h_erin "Let me help you with those."
    "She takes the bottles out of my hands and drags two shot glasses out of the cupboard, pouring vodka into each one."
    h_erin "Drink!"
    "She holds one out for me and I begrudgingly take it."
    paul "Awesome! We're starting the shots early!"
    
    show paul a_1 at left
    show h_mark a_1 at centerleft
    with easeinleft
    
    #paul + mark come in
    paul "Get another two going Erin."
    "She obliges and soon the four of us are on our forth one. I don't really want another after that, but people start arriving I decide {q} What the hell!{/q} and knock it back."
    think "I'm in for a hell of a long night anyway, may as well at least relax a bit."
    title "Two hours later."
    
    scene bg sayaka livingroom party
    show h_holly blush a_0 at center
    show h_erin blush a_0 at Position(xpos = (placement_of(h_holly).xpos + 0.15))
    
    "Erin has been clinging on me for the last few hours, as though I might evaporate, the large amount of alcohol I've consumed does nothing to make this less irritating."
    think "Her arm feels like it's been surgically attached to my waist.. although now she's stopped forcing her tongue down my throat, so the kissing has improved..."
    think "Either that.. or I'm too drunk to notice how bad it is.."
    
    show h_erin a_6
    
    h_erin "You wanna take this back to your place?"
    "She uses her tongue to trace around my ear as she says that in a playful voice."
    think "On one hand, I haven't had sex in forever and I know Erin is defiantly interested, regardless of the amount of alcohol in her system... but on the other, I can't shake the feeling that I'll seriously regret this in the morning. And I'm a firm believer in gut-feeling"
    
    show h_holly blush a_8
    
    holly "Um, maybe.. just give me one sec.."
    "I manage to excuse myself under the pretense of going to the bathroom and began a frantic search for Paul."
    
    scene black with fade
    scene bg sayaka kitchen night lights on
    show paul a_1 at centerright
    show h_holly blush a_6
    
    "I spot him playing some sort of drinking game in the kitchen"
    holly "Paul!!!"
    paul "H-ho-Holly! Howr.. things?"
    holly "I'm having a moral dilemma... That I think you might be too drunk to help me solve."
    paul "yoooor... your welecuame."
    
    show h_holly a_11
    
    holly "I think I'm gonna head home, I'll see you in the morning."
    
    show paul a_7
    
    paul "Make.. make sure you take Erin with you."
    #Paul -> holly.pos
    "He winks before pulling me into a hug"
    paul "She's well fit!"
    holly "I don't think I can Paul, It's been so long and I just don't fanc-"
    
    stop music fadeout 2.0
    
    paul "EYY. Lis-listen, Erin is hot, you're just nervous because it's been a whole long time since you've seen another naked women, or woman naked, whatever. Take Erin home and get back into the saddle! You know she likes you."
    
    show h_holly a_26
    
    "I can't help to smile, it took him three tries to get that sentence coherent.."
    "Perhaps he's right and I'm just nervous?? I gave up dating because I didn't feel emotionally stable enough to deal with it but I have been better lately.. and it isn't like I'm jumping into a relationship, just sex."
    
    scene black with fade
    play music h_bgm_omae fadein 2.0
    scene bg sayaka livingroom party
    
    "I locate my jacket and head back to where I last saw Erin, only to find her stood at the front door waiting for me."
    
    show h_erin a_8 at left
    show h_holly a_3 at centerleft
    
    h_erin "Leaving without me?"
    
    show h_holly a_1 
    
    holly "Of course.. not, I was just coming to find you. Shall we?"
    
    scene black with fade
    scene bg sayaka house night lights on
    show h_holly blush a_3
    show h_erin blush a_5 at Position(xpos = (placement_of(h_holly).xpos + 0.15))
    
    "We climb into a taxi and Erin sits right next to me, her lips on my neck and her hand on the top of my tight. I rest my hand on her knee slowly edge it further up her leg. My heart isn't really in it, but I tell myself that maybe I'll get into it if I keep trying."
    "..."
    
    scene black with fade
    
    title "A taxi ride later."
    
    scene bg connie bedroom clean night
    outfit h_holly nude
    outfit h_erin nude
    show h_holly blush a_3 at left
    show h_erin blush a_5 at Position(xpos = (placement_of(h_holly).xpos + 0.15))
    
    "Half an hour later we're in my bed, our clothes strewn across the floor and our hands all over each other. Despite Erin's best effort in the taxi I'm still not really feeling it. My insides are fluttering with nerves and anxiety, there's no excitement"
    "As soon as I'm able too I roll Erin onto her back and am thankful she allows me to take control of the situation. I slip my hand between her thighs and push two fingers straight into her, perhaps a little roughly but her loud moans indicate that she likes it."
    
    show h_erin b_6
    
    "Normally I'd take my time with this but right now all I want to do is sleep. I curl my fingers upwards searching for that magic spot and thankfully find it quickly. Erin's fingernails dig painfully into my back as I pump my fingers in and out of her."
    h_erin "Oh, fuck yes!"
    
    show h_erin b_18
    
    h_erin "I knew you'd be a good fuck Holly."
    "I slide my fingers in and out faster, using my thumb to rub her clit as I take her nipple between my teeth and bite down gently."
    
    show h_erin a_6
    
    h_erin "Harder Holly!"
    h_erin "That feels so good.. fuck me.. ahhh.. fuck me harder!"
    "I add a third finger and press into her as hard as I can, I feel her fingernails pierce the skin on my back and groan in pain, this seems to turn Erin on more as her legs wrap around my ass and her body starts to shake."
    "It only takes a few more seconds for her to cum."
    "Slowly I pull out of her and lay down on my back beside her, she doesn't try to speak, just lays there with a triumphant grin on her face. I watch her chest rise and fall, her breathing deepening with each breath."
    "Three minutes pass and she's out for the count."
    
    show h_erin a_2
    
    holly "That was quick.. luckily."
    "I said it in a quiet tone, hopefully she didn't hear. Exhausted, I roll onto my side and pull the duvet around me, Erin doesn't stir at the movement and instead starts to snore heavily."
    
    stop music fadeout 2.0
    show h_holly b_1
    
    "My long night doesn't look like it's going to end anytime soon."
    
    scene bg connie bedroom clean day
    show h_holly a_0
    
    "I wake up late the following morning. I finally managed to drift off at around three am and its now almost midday, much later than I'd normally sleep in at the weekend. 
    I turn over and am disappointed to find that Erin is still here...and still snoring...rolling over fully I note small spots of blood on my sheet from where Erin's fingernails pierced my skin...great, getting that out is going to take some doing..."
    
    outfit h_holly redtrack
    show h_holly a_3
    
    "It takes a few more minutes before I remember I'm meant to be meeting Haley today...shit!"
    
    scene bg sadie livingroom day
    outfit h_haley casual_b
    show h_holly a_35 at left with easeinleft
    show paul a_4 at right
    show h_haley b_15 at centerright
    
    paul "She lives!!"
    
    show h_holly a_15
    show paul a_0
    
    holly "Very funny."
    
    show h_holly a_9
    
    "Running my fingers through my hair and taking in the long, curly brunette hair of the woman I'm supposed to be trying to encourage to take our spare room."
    paul "Anyway, Haley this is Holly, Holly this is Haley. Although i guess if you remember each other introductions are pointless."
    
    show h_haley b_17 at centerright, faceleft
    
    "The woman turns around and I feel my breath catch in my throat, she's absolutely stunning! I can't believe I don't remember her! Her curly hair hangs casually over her shoulder framing her face and a sweeping fringe covers her brilliant hazel eyes. 
    One glance over the rest of her body is enough to see that she clearly works out."
    h_haley "Hi"
    
    show h_haley b_18
    
    "She extends her hand and smiles, revealing perfectly straight, white teeth"
    h_haley "Nice to see you again Holly."
    
    show h_holly at Position(xpos = (placement_of(h_haley).xpos - 0.15)) with move
    
    "I take her hand and instantly note her manicured nails and how soft her skin is."
    
    show h_holly blush a_1
    
    holly "h-hi, nice to see you again too."
    
    show h_holly blush a_1 at centerleft with move
    
    "It's not entirely a lie, it {b}{i}is{/i}{/b} nice to see her despite not remembering that we've met."
    holly "Sorry I'm not so awake this morning, {i}someone{/i}.."
    
    show h_holly a_2
    
    "I look pointedly across at Paul"
    holly "decided that going to a party the night before we met you was a great idea.."
    
    show h_haley b_17
    
    h_haley "No worries,"
    think "She smiles again.. God that smile is amazing..."
    h_haley "Did you have a good night?"
    
    show paul a_7
    
    paul "One of us did"
    
    show h_holly a_5
   
    holly "It was okay."
    "To further compound my embarrassment, Erin chooses this moment to come into the room wearing an old shirt of mine and not very much else."
    
    outfit h_erin swimsuit 
    show h_erin a_12 at Position(xpos = (placement_of(h_holly).xpos - 0.20)) with easeinleft
    show h_holly a_3
    
    h_erin "Morning beautiful."
    "She slides her hands around my hips and kisses my cheek"
    h_erin "I had an amazing time last night, we should definitely do this again sometime."
    "I can feel my face burning as she leaves the room."
    
    hide h_erin with easeoutleft
    show h_haley b_19
    
    h_haley "Sounds like it was more than okay."
    
    show h_holly blush a_3
    
    holly "Yeah.."
    
    show h_holly a_3
    
    paul "So, shall we give you a tour around the apartment?"
    
    show h_haley a_14
    
    h_haley "That'd be great"
    
    scene black with fade
    
    nvl clear
    nvl_narrator "An hour later we've somehow managed to convince Haley to take the spare room and arranged to help her move her things in the following morning."
    nvl_narrator "Erin left soon after the scene in the living room but not before embarrassing me again by sticking her tongue down my throat as a way of saying goodbye."
    nvl_narrator "Paul, of course, found this hilarious, but Haley took it in her stride and barely batted an eye. At least one of them could tell I was mortified!"
    
    title "Haley moves in."
    "Haley arrived bright eyed and bushy tailed the next morning ready to move in. Thankfully I made a better second impression and was up, dressed and eating breakfast as she pulled onto the drive. I dumped my bowl and spoon in the kitchen sink and went out to meet her"
    
    scene bg connie apartment day
    outfit h_holly casual 
    outfit h_haley casual
    show h_holly a_9 at centerleft with easeinleft
    show h_haley a_12 at centerright
    
    h_haley "Hey Holly. Feeling better this morning?"
    holly "Er, yes, thanks."
    
    show h_haley a_15 at centerright, faceright
    
    h_haley "You sure about that? You don't sound very convinced"
    holly "It's still early.."
    "I check at the small pile of boxes she brought."
    holly "This is all you've got?"
    
    show h_haley a_13
    
    h_haley "I travel light."
    "She takes the heaviest of the boxes with ease and turns towards the apartment."
    holly "I'll say.."
    "I take another, thankfully much lighter box and takes it into the apartment."
    
    hide h_holly
    hide h_haley
    with easeoutleft
   
    scene black with fade
    scene bg sadie livingroom day
   
    show h_holly a_9 at centerright
    show h_haley a_12 at center
    with easeinright

    h_haley "Thanks for helping with this Holly, I hope I'm not taking up to much of your time. Paul said you were studying for a degree?"
    "The muscles in her forearms flex a little as she adjusts the box to a more comfortable position."
    
    show h_holly a_0 at centerright, faceright
    
    holly "Oh, I am"
    holly "But i had my last exam of the year on Friday, just twelve months to go and then it's all over."
    
    show h_holly a_1 at centerright, faceleft
    
    h_haley "What's the degree in?"
    holly "Psychology, the human brain fascinates me."
    
    show h_haley b_4
    
    h_haley "Sounds interesting. If you ever figure out how the male brain works please let me know"
    holly "The male brain isn't really my main area of interest, sorry about that."
    h_haley "No worries, maybe i should let you tell me about the female brain instead?"
    holly "I don't really know much about that either, I'm mainly interested in the thought processes behind every day thinking."
    
    show h_haley b_16
    
    "I look across at Haley to find she's trying hard to contain herself... it takes further few long seconds before I realize I've completely missed the joke..."
    h_haley "It's okay, it was a horrible attempt at humor."
    
    show h_holly a_5
    
    holly "No.. it was a good joke, I'm just not with it yet today."
    
    show h_haley b_8
    
    h_haley "Are you okay Holly? Paul said you were going through a bit of a tough time and you might be different to how i remembered you, I'm sorry if I've upset you."
    holly "You remember me?"
    think "Why on earth would this goddess of a woman remember me..."
    
    show h_haley b_11
    
    h_haley "Of course"
    
    show h_holly b_2
    
    holly "Oh..."
    h_haley "Is that not okay?"
    holly "It is bu-"
    
    play sound sfx_alarm_warning
    show h_haley a_1
    
    h_haley "Shit! I've got to take this, we'll talk in a bit ok?"
    
    show h_holly b_4
    stop sound
    
    holly "Ok.."
    
    scene black with fade
    scene bg connie bedroom clean day
    show h_holly b_0:
        rotate 90
        zoom 0.8
        ypos 0.3
        xalign -0.4
    
    "I was laid on my bed that afternoon hugging my pillow while reliving my painful and embarrassing conversation with Haley, when a familiar voice filtered up from downstairs."
    temp_char "Holly!"
    "I stick my head out of the door and a huge smile erupts on my face as I confirm that it is actually Paul's girlfriend Bethany who's shouting me."
    
    show h_holly:
        rotate 0
    hide h_holly with easeoutright
    outfit h_bethany dress
    scene bg sadie livingroom day
    show h_bethany a_3 at centerright, faceleft
    
    holly "Bethany!!!"
    
    show h_holly a_1 at center with easeinleft
    
    "I basically crash into her open arms to get my customary bear hug."
    h_bethany "I missed you so much!"
    "She pulls me in tight and kiss my cheek"
    h_bethany "How did your exam go?"
    holly "I missed you too, how was your trip? My exam was fine thanks."
    h_bethany "It wa-"
    paul "I always knew I'd come home one day and find you two together."
    
    show h_bethany at centerleft
    show h_holly at left
    with move
    show paul a_1 at centerright
    show h_haley a_12 at right, faceleft
    with easeinright
    show h_bethany a_9
    
    h_bethany "He says, whilst walking through the door with a gorgeous brunette woman I don't know."
    "For extra effect she brushes my hair away from my face and kisses my forehead."
    paul "Oh shit, sorry babe. This is Haley, my friend from UNI and the answer to our roommate problem. Haley, this is my girl Bethany."
    
    show h_bethany a_3
    
    h_bethany "Hi Haley, I hope you know what you're in for, taking care of these two."
    h_haley "It's been ok so far." 
    
    show h_haley a_13
    
    h_haley "I don't think I've upset the boat too much in the eight hours since I moved in."
    holly "You haven't." 
    "I say to the floor as I wonder exactly how much Tommy's told her about my situation at the moment."
    h_bethany "Give it a few days and you'll be tearing your hair out."
    "I envy Bethany so much sometimes, she's so free and easy around new people while I'm an uptight, nervous wreck."
    paul "We're not that bad."
    h_bethany "That's what you think." 
    h_bethany "Hi baby. What're we doing for dinner?"
    paul "You fancy going out? Give us a chance to bond and all that crap."
    h_bethany "That'd be great." 
    paul "We should ask Erin to come too...don't you think Holly?"
    
    show h_holly b_4
    show h_bethany a_8
    
    "I could've died on the spot."
    "Bethany whips her head around so fast we hear her neck crick."
    h_bethany "What?!?!"
    holly "I'll tell you later." 
    "I mumble, deliberately avoiding her eyes."
    "I'll text her and let her know where to meet us then." 
    "Paul continues, using my lack of an answer as a yes and pulling out his phone, once again completely oblivious to the situation around him."
    "Bethany rounds on him a fraction of a second later shooting daggers. I use this as an out and escape back upstairs, followed closely by Haley."
    
    hide h_haley
    hide h_holly
    with easeoutleft
    scene bg connie bedroom clean day
    show h_haley a_9 at centerleft
    show h_holly a_3 at centerright
    with easeinright
    
    h_haley "She really doesn't like Erin then?"
    holly "Doesn't like is a mild understatement. She can't stand her...and Beth loves everyone."
    h_haley "Do you like her? Erin, that is."
    holly "Ermmm... I think, I mean, I don't really know her that well, but I guess she's attractive and she likes me so..."
    
    show h_haley a_15
    
    h_haley "So that's enough for you?"
    holly "I don't know," 
    
    show h_holly a_8
    
    holly "I haven't really dated for a while. Maybe someone who I know is definitely interested is a good place to start?"
    "She shakes her head and stands up straight again."
    h_haley "I'm sure if women knew you were available they'd be queueing round the block to get a date with you...and you never know, you might actually like one of them."
    holly "Maybe..."
    h_haley "Trust me," 
    
    show h_haley a_2
    
    h_haley "you're gorgeous Holly. Inside and out if I remember rightly. You could have whoever you wanted..."
    
    scene black with fade
    
    "Dinner was awful."
    
    scene bg bar dusk
    
    nvl clear
    nvl_narrator "Erin met us at the restaurant and continued her customary tradition of shoving her tongue down my throat which had me instantly embarrassed and Bethany instantly annoyed. One look was all it took for me to know I was in for a serious talk with her as soon as we got home."
    nvl_narrator "We got through the main course in virtual silence, every time anyone asked Haley a question Erin would talk over her and try to block her from the conversation, it got so awkward that silence was the best solution."
    nvl_narrator "A little later on, Haley braved speaking again invited me to join her for a climbing session next time she went, I thought it sounded interesting and agreed to go...Erin on the other hand, saw red and stormed off outside to 'make a call'...I think I was supposed to follow her and reassure her that despite us only spending one night together, she was my one and only, but to be honest, I was just happy for the break. The atmosphere was so tense you could have cut the air with a knife, and even though I hadn't invited her, I felt like the whole situation Erin had caused was my fault."
    nvl_narrator "The evening was rounded off nicely by her leaving just before we did, skipping out on her share of the bill."
    
    scene black with fade
    scene bg connie bedroom clean night
    
    "After we came home Haley went straight to her room, Bethany and Paul went into an argument in the kitchen about me and Erin, I knew they'd both acted with my best interests at heart, but I fell asleep wishing that they'd all just let me suffer alone in my bubble until I figured things out. I hated that I'd caused so much trouble."
    title "Session"
    
    scene bg corporate lobby small
    play music h_bgm_issues
    show h_holly b_7 at centerleft
    show h_kisaragi a_3 at centerright
    
    h_kisaragi "How have you been since our last session?"
    holly "Erm, ok I guess. We've got a new house mate...and we nearly had World War Three the first night after she moved in."
    h_kisaragi "Are the two things related?"
    holly "Um, no...not really."
    h_kisaragi "Ok, well why don't we start with World War Three and end with a hopefully more positive story?"
    "I take a deep breath, feeling me entire chest puff up"
    h_kisaragi "I know it's hard Holly,"
    
    show h_kisaragi a_8
    
    h_kisaragi "but I can't help you if you don't speak."
    "I look down at my hands and twiddle my thumbs, weighing up my options."
    h_kisaragi "I need you to be honest too Holly,"
    h_kisaragi "I don't care if you get upset and we have to use a whole box of tissues to get through it. Omitting details will only lead to bigger issues building up."
    h_kisaragi "Ready?"
    
    show h_holly b_8
    
    holly "Yes.."
    "Fifteen fraught minutes later I've told Blaire everything...about the party...Erin...dinner...Erin...and the after-dinner showdown when we got home...that also concerned Erin."
    
    show h_holly b_9
    show h_kisaragi a_9
    
    h_kisaragi "Wow."
    holly "Now you see why I'm not sociable. Things go tits-up when I leave the house."
    
    show h_kisaragi c_1
    
    h_kisaragi "How did you feel, about going out and then spending the night with Erin?"
    holly "Erm.."
    holly "..."
    holly "Well, at first I felt nervous and awkward about going out, and even though I know Mark really well it was hard to relax. Hence why I decided that drink was a good idea...and why I ended up with Erin."
    h_kisaragi "What about your night with Erin, how did that make you feel?"
    holly "It didn't really," 
    holly "It's like, I was there but I wasn't at the same time. I didn't really enjoy the experience. I just did what I needed to do for it to be over."
    h_kisaragi "Do you think that's healthy?"
    holly "Definitely not."
    "I reply quickly, trying to find the words she wants to hear before she asks me any further questions on the topic"
    holly "But there's only me that can get myself out of it and fix the situation...and I need to tell Paul to back off"
    
    show h_kisaragi b_4
    
    h_kisaragi "And what is it important to remember?"
    holly "To give myself a break...and that change doesn't happen overnight."
    
    show h_kisaragi b_6
    
    h_kisaragi "Good." 
    h_kisaragi "Now, let's move on to more positive conversation. How's Haley working out as a new house mate, is she fitting in well with the three of you?"
    holly "Well, she's a friend of Paul's from University and I think they've lived together before, so he's fine, then Bethany gets on with everyone so she's fine too."
    h_kisaragi "And what about you?"
    h_kisaragi "How are you finding having someone new in your home?"
    holly "It's fine,"
    holly "I keep to myself and we work different hours so there's never a clash for the bathroom. I can't say I've really noticed her being there to be honest."
    h_kisaragi "So basically, everyone's fine and you've not spoken to her at all?" 
    
    show h_kisaragi b_11
    
    h_kisaragi "Things get easier the more you do them Holly."
    holly "I know," 
    holly "but I spoke to her briefly when she moved in, helped her move some boxes. It wasn't as traumatic as expected."
    h_kisaragi "Has she tried to speak to you at all?"
    holly "Um, yeah we chatted a bit while I helped her move things and then a bit more at dinner. She asked about my degree stuff and offered to take me climbing with her next time she goes."
    h_kisaragi "That sounds good," 
    
    show h_kisaragi b_8
    
    h_kisaragi "It sounds as though she wants to get to know you."
    
    show h_holly b_5 at faceleft
    
    h_kisaragi "What does that mean, what're you thinking?"
    think "Breath in Holly you can do this."
    holly "That she's just making an effort because she's friends with Paul, she doesn't really want to know me."
    
    show h_kisaragi b_1
    
    h_kisaragi "Why wouldn't she want to know you?"
    
    show h_holly b_9 at faceright
    
    holly "Because I'm really boring and she's this gorgeous, super fit, action woman who probably doesn't need any extra friends...let alone boring, depressed, sad, lonely ones."
    h_kisaragi "And how do you know this?"
    holly "Because I-" 
    
    show h_kisaragi b_8
    
    "I stop abruptly as I realize what it is she's driving at and look up to see her smiling at me"
    holly "I don't."
    h_kisaragi "Exactly,"
    
    show h_kisaragi b_6
    
    h_kisaragi "it sounds to me like Haley has plenty of friends and an active social life. If she didn't want to know you, she wouldn't make any effort to try."
    
    show h_holly b_1
    
    holly "She does seem to remember me from when we met years ago..."
    h_kisaragi "I keep telling you that you're worth knowing Holly, I certainly like to see you every week. There's absolutely no reason why Haley wouldn't feel the same way."
    
    show h_holly blush b_1
    
    h_kisaragi "So, there's your homework for the week." 
    h_kisaragi "Practice letting people get to know you a little bit more, think about how you're going to deal with the Erin situation and then next week you can tell me all about it."
    
    scene black with fade
    #Make this part more intressting, add images.
    
    nvl clear
    nvl_narrator "Following Blaire's advice, I made much more of an effort to let people in, not just over the week between that initial session and the next, but over the next few months as well. And not just with Haley, with everyone else too."
    nvl_narrator "It was almost impossible at first, but gradually I managed to speak more and more and volunteered information about myself without other people needing to prize it out of me. It had definitely made life at home better, Bethany and Paul had known me long enough that they knew what I was like, but for Haley I must have seemed like a completely different person to the one she met back in June."
    nvl_narrator "For the first time in years I actually enjoyed Christmas. Normally the thought of so much social activity filled me with nothing but anxiety and I spent a considerable amount of time wishing the whole festive period away."
    nvl_narrator "But this year it was just...well...fun. Our {q}House Mates Only{/q} Christmas party was great and really set the whole holiday up, it was nice for there to be four of us. Haley had slotted in perfectly with us and it was a welcome change to have someone on my team while playing games and someone to sit up with once Bethany and Paul went to bed. My family even commented on how much better I seemed during the few days I spent with them."
    nvl_narrator "The only problem was Erin."
    nvl clear
    nvl_narrator "I had tried for a while to give her the benefit of the doubt and to open up around her...much to Bethany's disgust...and had even ventured as far as telling her about my counseling sessions, but she just wasn't interested. She only showed an interest when Haley was around."
    nvl_narrator "Jayne was also surprised by my continued relationship with Erin, she was a frequent topic of conversation during our sessions and had yet to be a positive subject. I think personally she agreed with Bethany and felt that I should end things with her, but due to the nature of our relationship she was professionally unable to give her true opinion."
    nvl_narrator "I hadn't seen Erin over Christmas, but had given her her gift just after. She hadn't got me a present and again failed to give me anything during the sex afterwards, instead she had let me get her off and then spent the next half hour roundly abusing the thoughtful book Haley had bought me."
    nvl_narrator "I saw red at that point and for the first time in six months bit back. It didn't go down well to say the least. I left the house to a torrent of verbal abuse, which ended in her telling me she wished I was dead, and then spent the evening in Bethany's arms while she calmed me down and wiped the angry tears from my face."
    
    scene black with fade
    scene bg connie kitchen day
    
    "On the Monday after the argument with Erin, I walked in after a long, boring day at work to find Paul, Mark, Erin and Haley sat at our kitchen table passing a bottle of whiskey between themselves."
    
    outfit h_erin casual
    show paul a_0 at left:
        zoom 0.8
    show h_haley a_1 at centerleft:
        zoom 0.8
    show h_mark a_0:
        zoom 0.8
        xalign placement_of(paul).xpos + (placement_of(h_haley).xpos / 1.5)
        yalign placement_of(paul).ypos
    show h_erin a_0:
        zoom 0.8
        xalign placement_of(paul).xpos - placement_of(h_haley).xpos
        yalign placement_of(h_haley).ypos
    
    paul "Holly! Come drink with us!"
    holly "No than-" 
    "I start, glaring at Paul over the top of Erin's head. What the fuck is she doing here!"
    
    show h_haley a_12
    
    h_haley "Please Holly. You look like you could use one."
    "I begrudgingly sit down in the empty seat between Erin and Mark and Paul hands me the bottle, instructing me to take a big swig. Unfortunately, Erin chooses this moment to squeeze my knee causing me to choke on the already burning liquid."
    
    show h_holly b_0 at center, faceleft with easeinleft:
        zoom 0.8
    
    h_mark "Steady on! "
    holly "So- sorry."
    think "I shoot Erin a confused look. She wished me dead not seven days ago and now she wants to be friends again? What the fuck?!"
    holly "Where's Bethany?"
    paul "Out for dinner with a friend, she'll be back later, don't panic."
    h_erin "Jesus, it's nothing to worry about,"
    
    show h_erin a_12
    
    h_erin "She's got a life away from you you know."
    "I don't acknowledge her comment, I know she's trying to get me to bite again. But her words stir some dark feelings within me that I thought I was finally making some progress in getting over..."
    
    scene black with fade
    scene bg connie kitchen day
    
    "An hour later the first bottle of whiskey is gone and a second one appears from nowhere. I can already feel myself buzzing from the first bottle and take this as my cue to leave. I try to stand from the table but am quickly intercepted by Erin."
    
    show paul a_0 at left:
        zoom 0.8
    show h_haley a_1 at centerleft:
        zoom 0.8
    show h_mark a_0:
        zoom 0.8
        xalign placement_of(paul).xpos + (placement_of(h_haley).xpos / 1.5)
        yalign placement_of(paul).ypos
    show h_erin a_0:
        zoom 0.8
        xalign placement_of(paul).xpos - placement_of(h_haley).xpos
        yalign placement_of(h_haley).ypos
    show h_holly b_0 at center, faceleft:
        zoom 0.8
    
    h_erin "No you don't."
    h_erin "We're playing spin the bottle!"
    holly "Spin the bottle? What are we, escapees from a classic teen movie?"
    h_erin "Don't be such a spoilsport! Ok everyone! No kissing with tongue for those of us that are attached...otherwise, anything goes."
    
    show h_haley a_2
    
    h_haley "Won't this be the most pointless game ever though? You know, since most of us..." 
    "she glares pointedly at Erin" 
    h_haley "Are actually attached."
    
    show h_erin a_3
    
    h_erin "There's no wonder you're single with an attitude like that!"
    
    show h_mark a_2
   
    h_mark "Ok, ok guys. Let's just play, ok?"
    "Satisfied that she'd won that round and sufficiently upset Haley, and with those as the only two rules, Erin took the bottle and started us off, promptly leaning across me to plant a kiss that clearly involved her tongue on Mark after her first spin."
    think "I didn't even bother acknowledging her, I knew it was yet another ploy to get me to bite, but I was far more concerned with trying to figure out why I was willing to put up with this shit..."
    "Time seemed to stop as we played, I'm not sure if the others felt the same way I did or not, but I couldn't wait to get out of there. I gave it another half hour before deciding that enough was enough and was half way out of my chair before I realized that Haley was staring intently at me."
    holly "What?"
    
    show h_haley a_7
    
    h_haley "You need to give me a kiss Holly. Her eyes blazing into mine"
    
    show h_holly blush b_4
    
    "We must've been playing for a while but this is the first time she or I had spun each other."
    holly "Guys, I'm really tired. I just want to go to bed."
    h_mark "One more kiss Holly, then you can go to bed," 
    
    show h_mark a_5
    
    h_mark "Haley been waiting for this all night." 
    "He winks at her causing her to blush...and Erin's face to drop."
    
    hide h_haley
    show h_haley blush a_6 at centerleft, faceright:
        zoom 0.8
    show h_erin b_1
    
    holly "Ok fine."
    
    hide h_holly
    show h_holly a_14 at center, faceleft:
        zoom 0.8
    
    "I sigh, desperate to get out of this situation...and to save Haley any further embarrassment."  
    
    show h_holly blush b_4 at faceleft:
        xpos placement_of(h_haley).xpos
        ypos placement_of(h_haley).ypos + 0.06
    with move
    
    h_mark "Wow Holly,"
    
    show h_mark a_2
    
    h_mark "I've seen people give their grandmas more passionate kisses."
    
    show h_haley a_8
    
    "I look back down at Haley to see she's even more embarrassed...and visibly hurt...which is the last thing I wanted."
    
    show h_mark a_2
    
    "I walk around the table and lean down to kiss her. She closes her eyes and I close the distance between us, pecking her lips lightly. I pull away quickly and notice that her eyes are still closed..."
    
    scene h_asset kiss with dissolve
    
    nvl clear
    nvl_narrator "Cursing silently, I lick my lips nervously, thankful that they aren't as chapped and sore as they once were. My eyes flick across the table at Erin and I suddenly feel a bit rebellious, if she can break her own rules, why can't I? I turn back to Haley and cup her face in my hands. Leaning in slowly I lightly press my lips to hers once more and feel her mouth move against mine. I use the tip of my tongue to gently part her lips and she moans softly, her tongue reaches out to meet mine and I get a slight taste of whiskey as her arms wrap around my neck."
    nvl_narrator "Haley's grip intensifies around my neck and my fingers slide unconsciously into her silky brunette locks, it feels as though the rest of the world slips away as we continue our kiss...that is until the sound of an angry cough from the other side of the table meets our ears."
    nvl_narrator "I pull abruptly away from Haley and glance across the table to see Erin's face has gone from annoyed, to absolutely fuming, while Mark and Paul sport identical huge, gleeful yet surprised grins."
    nvl_narrator "What the hell was I thinking?! Excusing myself quickly I head upstairs without speaking to anyone and lock myself in my room, the last thing I need right now is another slanging match with Erin or to sit around the table with those two idiots grinning at me."
    
    hide h_holly easeoutright
    outfit h_haley gym
    scene black with fade
    scene bg sadie livingroom day
    show h_haley a_15 at centerleft, faceright
    show h_holly b_0 at centerright, faceleft with easeinright
    
    "I slope through the door at home on Friday and slink down the hall to the kitchen with the intention of repeating my routine and grabbing some food before retiring to the comfort of my room...only to be met by Haley coming the other way."
    h_haley "Hi Holly, you okay?"
    
    show h_holly b_2
    
    holly "Um, yeah.."
    h_haley "I've hardly seen you since Monday night, busy week?"
    h_holly "Kind of, I've had a steady stream of stuff to do." 
    "I shuffle my feet awkwardly and try not to stare too hard at her legs in her running shorts."
    h_haley "Ok..." 
    
    show h_haley a_2
    
    h_haley "Are you sure things are ok Holly? You haven't answered my texts and you're avoiding us all. Please don't tell me you're still embarrassed about that kiss, it was just a game...a great kiss...but just a game...and Erin can go fuck herself if she's said anything horrible to you! An-"
    
    show h_holly b_5 at centerright:
        ease 0.15 ypos (placement_of(h_holly).ypos - 0.05)
        ypos placement_of(h_holly).ypos

    "She stops suddenly and looks at me. At the mention of Erin I felt myself recoil and clearly she's seen it too."
    
    show h_haley a_7
    
    h_haley "Am I right on the money?"
    
    show h_holly b_4
    
    holly "... Yes."
    
    show h_haley blush a_7:
        ease 0.5 xpos placement_of(h_holly).xpos - 0.10
        xpos placement_of(h_holly).xpos - 0.10
    
    "She steps closer to me and wraps her arms around me. Her embrace is surprisingly soft; with all the exercise she does and the whole army thing, I was expecting it to be a bit rougher around the edges."
    holly "You're right about everything." 
    holly "Well, maybe not Erin, I haven't looked at any of my messages but I can almost guarantee there'll be something in there from her."
    
    show h_haley a_5:
        ease 0.3 xpos placement_of(h_holly).xpos - 0.25
        xpos placement_of(h_holly).xpos - 0.25
    
    "You want me to look through them with you?"
    
    show h_holly b_1
    
    holly "Thanks, but I can handle it. I think actually it might be time to grow a pair and tell her to fuck off."
    h_haley "That- that sounds like a really sensible idea. If you need me though, you know where I am."
    "I nod and give her a small smile which she returns as she plants a kiss on my cheek before heading out, leaving me to continue getting some dinner sorted."
    
    hide h_haley with easeoutright
    hide h_holly with easeoutleft
    scene black with fade
    scene bg connie kitchen day
    show h_holly b_0 at faceright:
        zoom 0.8
        ypos 0.3
        xalign 0

    "Twenty minutes later I find myself sat in the kitchen finishing off my dinner while reliving my conversation with Haley, how is it that she's known me for like six months and she knows me so well? One of my issues is not letting people get close, what makes her so special that she can read me like a book?"
    "A knock on the front door draws me out of my trance" 
    
    hide h_holly with easeoutright
    scene bg sadie livingroom day
    show h_holly b_0 at centerright, faceright with easeinleft
    show dominic b_0 at right:
    
    dominic "Hi, Haley around?" 
    "His voice is gruff and strained, as though he's spent a lot of time screaming at someone recently."
    holly "She might be," 
    "Instantly i disliked this new person."
    "Depends on who you are?"
    h_haley "It's alright Holly,"
    
    outfit h_haley casual_b
    show h_haley a_4 at left, faceright with easeinleft
    
    h_haley "This is Dominic."
    holly "Your ex?"
    
    show dominic a_2
    
    dominic "Her current boyfriend." 
    "He strode up to Haley and plants a kiss on her lips"
    
    show dominic a_0 at left with move
    show h_holly b_0 at centerright, faceleft
    
    dominic "isn't that right babe?"
    
    show h_haley a_5
    
    h_haley "Um, yeah."
    "He drags her up the stairs towards her room leaving me standing alone next to the open front door."
    
    hide h_haley
    hide dominic
    with easeoutleft
    show h_holly b_4
    outfit h_bethany dress
    
    "I pause for a bewildered few seconds before hearing more footsteps coming up the drive."
    
    show h_bethany a_0 at right
    show paul a_0 at center
    with easeinright
    
    paul "Why hello there Holly."
    h_bethany "What's wrong with you?"
    holly "I just met Dominic."
    h_bethany "Want a drink?"
    
    show h_holly b_1
    
    holly "I think i need one.. yeah."
    
    scene bg connie kitchen day with dissolve
    
    "Once in the kitchen Bethany rounds on me almost immediately."
    
    show h_bethany a_8 at left
    show h_holly b_0 at centerleft, faceleft
    with easeinright
    
    h_bethany "So, Dominic, what do you think?"
    holly "Not a lot to be honest, although the conversation was brie-"
    h_bethany "Brief is long enough. Now, what's your plan?"
    holly "My- my plan?"
    h_bethany "To break them up." 
    
    show h_bethany a_11
    
    "She raises her eyebrows at me as though there's something I'm seriously missing."
    holly "Bethany, I've got no idea what you're talking about. Why would I have a plan to break them up?"
    h_bethany "Now I'm confused...Haley said you guys kissed?"
    holly "During a drunken game of spin the bottle we did," 
    
    show h_holly b_1
    
    "I laugh"
    holly "it was nothing serious."
    h_bethany "Spin the bottle? Which classic teen movie did you escape from?"
    holly "That's exactly what I said."
    
    show h_holly b_10
    
    "I laugh even harder."
    h_bethany "Well, Haley certainly described it as more than a drunken kiss."
    "That sobers me up instantly."
    
    show h_holly b_2
    
    holly "She told you about it?" 
    h_bethany "More like described it in loving detail actually."
    
    show h_bethany b_9
    
    "You certainly made an impression."
    
    show h_holly blush b_2
    
    "I can feel my face coloring and my cheeks starting to burn."
    h_bethany "Why do you think she called that dickhead and got back together with him?"
    holly "Because she's realized, I'm not as good at kissing as she thought?"
    
    show h_bethany b_8
    
    h_bethany "For someone who's doing a psychology degree you're pretty fucking dense Holly." 
    h_bethany "Don't worry, it'll all make sense when you're older." 
    "She pinches my cheek and turns to the kettle to start making drinks."
    holly "Or maybe she just wanted to get back with him because she misses him?"
    holly "Ok, so maybe not for that reason...perhaps she's just lonely...or after an easy lay."
    
    show h_bethany b_16
    
    h_bethany "Now that sounds familiar." 
    holly "Erin is a completely different situation!"
    
    show h_holly b_5
    
    holly "I had no intention of going there in the first place. It was Brad and alcohol that caused this mess."
    h_bethany "And a little bit of you dropping your knickers...right?"
    
    show h_holly b_6
    
    holly "Actually, it's kind of just been her dropping her knickers..." 
    
    show h_bethany b_13
    
    h_bethany "What?! I knew it'd be a one-sided affair!"
    
    show h_holly b_7
    
    holly "It is what it is, I'm trying to get out of it. I've just not got as far as how yet..."
    
    show h_bethany b_11
    
    "She sighs deeply."
    h_bethany "It may surprise you to hear this Holly, but you are actually a really good catch. There's a reason she's clinging on to you...and it's not just because she likes letting you get her off."
    holly "Thanks Beth." 
    "I give her a hug."
    
    show paul a_7 at centerright, faceleft
    
    paul "Group hug is it?" 
    
    show paul at center with move
    
    "Paul's voice barely has chance to reach my ears before I feel him jump on my back and wrap his arms around both me and his girlfriend."
    h_bethany "Ouch! Get off Brad, you idiot!"
    
    scene bg sadie livingroom day with dissolve
    show h_holly b_3 at right, faceleft
    show h_bethany b_8 at centerright
    show paul a_0 at center
    
    "Ten minutes later we're in the front room trying to watch TV and catch up, it feels like ages since we've all just sat and talked. This proves difficult however as our voices are drowned out by the increasing volume coming from upstairs."
    holly "Do you think they'll ever stop?"
    "I ask, the noise starting to get to me."
    
    show paul a_2
    
    paul "Sounds like they're having a hell of a reunion." 
    "Paul winks at me before Bethany slaps him playfully on the arm."
    
    show h_bethany b_0
    
    h_bethany "They'll be done soon if Haley knows Dominic." 
    
    show paul a_0
    
    paul "How do you know?"
    h_bethany "Girls talk Paul. You should know that by now." 
    
    show h_bethany at faceleft
    
    "She kisses his cheek."
    
    show h_bethany at faceright
    show h_holly b_8
    
    holly "How much longer is soon?!"
    "She glances at the clock"
    h_bethany "He arrived just before we did?" 
    holly "Mmhm"
    h_bethany "Then...another five minutes...at best."
    "After that we sit in silence and literally watch the clock, all of us now genuinely interested in the outcome."
    "The noise lasts another three minutes and fifteen seconds before the music stops and Dominic comes bouncing downstairs pulling his shirt back on."
    
    show h_bethany b_8 at faceleft
    show paul a_0 at faceleft
    outfit dominic swimsuit
    show dominic a_0 at left
    
    dominic "Later guys!"
    
    outfit dominic gym
    
    "He shouts, not even remotely concerned by the fact that the three of us are all staring intently at him from our position in the room."
    
    hide dominic with easeoutright
    show paul at faceright
    show h_bethany b_4 at faceright
    show h_holly b_10
    
    "We turn to look at each other and both Bethany and I start to laugh uncontrollably. Paul on the other hand looks deep in thought, his baby blue eyes full of concern."
    
    show h_bethany at faceleft
    
    h_bethany "What's the matter sweetheart?"
    
    show paul a_3
    
    paul "D- do you talk about how long we...you know...go for?" 
    h_bethany "What do you mean?"
    paul "Like Dominic, we all know now that he lasts twenty-five minutes. Do you tell people stuff like that?"
    
    show h_bethany b_16
    
    h_bethany "Of course not honey!" 
    "She replies, trying desperately to keep a straight face"
    
    show h_bethany b_15
    
    h_bethany "Once you get to below four minutes it's not even funny anymore, people just feel sorry for you."
    "Unable to keep a smile off my face any longer I let out a snort of laughter which is followed by even more uncontrollable giggling from Bethany. Paul, on the other hand, finds this far from amusing and storms out in a huff."
    
    hide paul with easeoutleft
    scene black with fade
    
    image bg connie bedroom blur = im.Blur('images/bg/connie bedroom clean night.png', 3.0)
    
    scene bg connie bedroom blur
    
    "By the time I head to bed that night I'm feeling better than I have all week, I almost feel happy and secure again, so happy and secure in fact, that I decide to check through the messages I haven't picked up all week...which is of course when it all comes crashing down around me."
    #$ screenfilter.blur = 10
    "I had a few messages from work colleagues about going for drinks...missed those...ah well...a couple of texts from Bethany...several texts from Paul, which all turned out to be about my kiss with Haley and how hot it was...then came the messages from Erin..."
    
    show h_erin b_3:
        zoom 2
        ypos 0.1
        xpos 0.1
    
    "Tuesday and Wednesday's messages started off with warnings and abusive language, don't dare kiss that fucking skank bitch again, that sort of thing."
    "By the early hours of Thursday morning they had progressed to insults about my family and friends...with the language decreasing further...Thursday night and the messages from today however, were a whole different ball game."
    "The language was disgusting, the insults had become personal and centered a lot around my depression and anxiety...with the worst of them being that I was a waste of life and I should end it all before I dragged everyone I cared about down with me."
    "The positive mood I had been in left me as soon as I read those messages, I knew I should just ignore her, that she wasn't worth bothering over, but in my fragile emotional state the words hit me like a brick and I quickly crumbled into an irrational, crying, shaking mess."
    
    hide h_erin with dissolve
    
    image bg connie bedroom clean dark = im.MatrixColor("images/bg/connie bedroom clean night.png", im.matrix.tint(0.15, 0.3, 0.45))
    
    scene bg connie bedroom clean dark with dissolve
    
    "I barely slept that night, tossing and turning until it was light enough to justify going for a walk. I thought a lot about my current situation as I walked, the progress I was making with counseling, how amazing Christmas had been and how I was slowly getting myself back on track." 
    "I resolved to try and ignore the messages that Erin had sent and made myself promise to call her when I got home to end things officially."
    "I knew she was a nasty, insensitive piece of work...and deep down I had always known it would end in tears...this didn't really cheer me up too much though, if I'd known that why had I been stupid enough to get myself involved in the first place? Was I really that desperate to have someone that I was prepared to walk on eggshells all the time and put up with being spoken to the way I had been?"
    "Blaire was always telling me I had to treat myself like I would a friend. Would I encourage a mate stay in a relationship like this? The answer was clearly no. Erin brought nothing into my life that made it better, she didn't really even have any redeeming qualities, other than that she was hot, in the conventional sense of the word."
    "The thought of being alone again was far from a pleasant one, but enough was enough, if I'd encourage a friend to get out than I'd be a hypocrite to ignore my own advice!"
    
    scene h_bg dusk with dissolve
    
    "After work the following day, I cried all the way home. I tried to tell myself that it was just relief that I'd finally figured out my next move, but I knew I was really just terrified of being alone again."
    
    scene bg sadie livingroom day with fade
    show h_holly b_9 at right, faceleft
    
    #phone_call_icon_dialing do some discussion mby?
    "I stuck to my guns though. As soon as I walked through the door I called Erin and told her it was over. She screamed and yelled and told me I should drop dead, just as she had done as I'd left on the day I gave her her Christmas present, but this time I was stronger, I held my nerve and didn't break my resolve."
    "After the phone call I was a wreck, I needed a stiff drink to try and calm my nerves, I didn't care that it was only 16:30. I grabbed a drink and the box of tissues before plopping myself down on the sofa and proceeding to cry my eyes out."
    
    show h_holly b_9:
        zoom 0.5
        yalign 0.7
        xalign 0.75
        faceright
    with move
    show h_bethany b_13 at right, faceleft 
    with easeinright
    
    h_bethany "Holly honey, what's the matter?!"
    "Beth shouts as she enters the room an hour later, quickly sitting down beside me on the sofa."
    
    show h_bethany b_6:
        zoom 0.5
        xpos placement_of(h_holly).xpos + 0.06
        ypos placement_of(h_holly).ypos + 0.15
    with move
    
    holly "Do you think I'm a waste of life?"
    "I whisper quietly, tears dripping down my cheeks."
    h_bethany "Of course I don't think you're a waste of life! Come here. Where on earth have you got that from?" 
    "She replies and pulls me firmly into her chest"
    holly "Erin..."
    h_bethany "Oh sweetie," 
    "She looks down at me, her eyes full of warmth and comfort"
    h_bethany "anything that bitch has to say you can ignore. I've hated her from the start, I could never understand why Paul always tried to push you two together! I hope you told her to piss off!"
    holly "I did, she got angry and started screaming abuse at me...and normally I wouldn't care, but you know when everything else is just so-"
    h_bethany "Hey, you've worked so hard to get yourself away from feeling like this, don't let Erin ruin it all for you!"
    "The door to the front room opens and Haley walks into the room nursing her right hand."
    
    outfit h_haley coat
    show h_haley a_10 at right, faceleft with easeinright
    
    h_bethany "What happened to you?"
    h_haley "I met Erin as I was leaving the gym..." 
    
    hide h_haley with easeoutleft
    
    "She replies darkly heading through to the kitchen."
    h_bethany "And?"
    h_haley "And..."
    
    show h_haley a_8 at left with easeinleft
    
    "Haley continues, re-entering the room with a bag of frozen peas on her hand"
    h_haley "She insulted one of my closest friends...so I socked her one."
    
    show h_bethany b_16
    
    h_bethany "Wow. You see Holly, people don't just sock other people on the street for people who are a waste of life!"
    
    show h_haley a_11
    
    h_haley "She called you a waste of life?! Hold this,"
    "She throws the peas to me" 
    h_haley "I'm gonna go find her and sock her again!"
    
    show h_holly blush b_1
    
    holly "That's ok, once was great, thanks Haley." 
    
    show h_holly blush b_1 at centerleft, faceleft:
        zoom 1
    with move
    
    "I kiss her cheek and hand her the peas back."
    
    image bg sadie livingroom day blur = im.Blur('images/bg/sadie livingroom day.png', 3.0)
    
    scene bg sadie livingroom day blur with dissolve
    
    "The rest of the day was spent drinking and roundly abusing Erin, Bethany bought us a takeaway dinner and I fell happily asleep on the sofa with my best friends either side of me."
    "I knew the feeling wouldn't last and I'd probably wake up feeling down...again...but nothing could've prepared me for just how much things would slide over the coming few days."
    
    title "The last few steps to rock bottom"
    
    scene h_bg star with dissolve
    
    "Bethany, Paul and Haley spent Sunday packing. By unfortunate coincidence all three of them were going away at the same time...as were my parents and Blaire ..."
    "Haley was off on a climbing trip with some friends, while Bethany and Paul were going on holiday for their anniversary...meaning I would be left alone."
    "The thought of being alone in itself wasn't what was bothering me, it was the emotions that came with it that had me worried."
    "I was already fragile and prone to tears, ten days by myself was the last thing I needed, I thought that perhaps I should talk about my worries...but after seeing how excited the others were about their various trips I was determined to stick it out and take care of myself, I didn't want them worrying about me..."
    
    scene bg sadie livingroom day with dissolve
    
    "Haley left in the early hours of the morning, she didn't make much noise but I was already awake, tossing and turning, trying to get my brain to switch off."
    "Two hours later Bethany and Paul were also ready to go."
    
    show h_bethany a_0 at centerright
    show h_holly b_0 at center
    with dissolve
    
    h_bethany "You sure you'll be ok?"
    
    show h_holly b_1
    
    holly "I'll be fine, I promise."
    
    show h_bethany a_6
    
    h_bethany "You look shattered"
    holly "I didn't sleep well last night; I might go back to bed for a bit."
    h_bethany "That sounds like a good idea, are you seeing Blaire while we're away?"
    holly "No, she's on holiday too so I'm not seeing her for another three weeks."
    
    show h_bethany a_3
    
    h_bethany "Ok, well, enjoy the peace and quiet while we're away and we'll see you in ten days."
    holly "Have a great trip Beth"
    h_bethany "See you soon Holly."
    holly "Bye."
    "She gives me warm hug and plants a kiss on my forehead"
    
    hide h_bethany with easeoutright
    show h_holly b_6
    
    "I watch from the empty living room as she walks out the door, a strange sensation starting in my chest as my insides begin to feel tight. I know I'm perfectly capable of surviving for a week and a half by myself but the way I've been feeling the last few days means I also know this is likely going to feel like a lot longer."
    
    title "Ten days later."
    
    scene h_asset sorrow
    
    nvl clear
    nvl_narrator "Things have spiraled quickly from OK, to really not OK."
    nvl_narrator "I tried so hard to keep on top of things, to make sure I ate properly, had some social interaction, got out of the house for a quick walk after work and went to bed on time. I managed it for a couple of days, but after receiving more abusive messages from Erin my resolve quickly crumbled."
    nvl_narrator "I suffered three horrendous panic attacks on consecutive nights meaning that I didn't manage to drift off until the early hours and spent most of that time tossing and turning. This in turn meant that I was late for work, which lead to me feeling guilty, hopeless and as though I'd let everyone down. I was exhausted, mentally and physically drained and starting to feel like I was drowning in negative thoughts again."
    nvl_narrator "By the time I reached Sunday night I was a real mess, I couldn't sleep in my room anymore, it felt like the walls were closing in on me. I was hardly eating, I could feel myself getting thinner with each day that passed, leaving the house was next to impossible and I was almost constantly in tears."
    nvl_narrator "I struggled through Monday at work but called in sick after that. Luckily I had followed Blaire's advice and been honest about my situation at work, my boss had been great about everything and was more than happy to let me take some time off to get myself sorted."
    
    "Wednesday morning"
    "I look across at the clock to see it reads half past eight. Sitting up on the sofa I take a deep breath and assess the state of the room...it's not good...I've been using it as a base since sleeping in my room has become such a struggle, but keeping it tidy hasn't been really high on my list of priorities."
    "I slide off the sofa and head for the bathroom, taking a deep breath I splash some cold water on my face and start the process of tidying up."
    
    scene bg sadie livingroom day
    
    "By the time Beth and Paul arrive back at three that afternoon, the house is spotless and the constant activity has helped me to switch off my brain, meaning that I'm feeling a little bit better."
    "The front door opens and Bethany bursts through it."
    
    show h_bethany a_0 at centerright
    show paul a_0 at right, faceleft
    with easeinright
    
    h_bethany "HOLLY?!"
    holly "Hey guys."
    
    show h_holly b_8 at left with easeinleft
    
    paul "Why aren't you at work?"
    
    show h_holly b_3
    
    holly "Nice to see you too..." 
    h_bethany "Things aren't good again, are they?" 
    "Beth asks sympathetically."
    
    show h_holly b_1:
        alpha 1.0
        ease 1.0 xpos placement_of(h_bethany).xpos alpha 1.0
        xpos placement_of(h_bethany).xpos
        alpha 1.0
    
    "I shake my head and she pulls me into a tight hug."
    
    show h_holly b_1 at center with move
    show h_bethany a_2
    
    h_bethany "You feel so thin! Have you eaten nothing while we've been away?!"
    holly "I- I tried..." 
    "I stammer as the tears start"
    
    show h_holly b_9
    
    holly "bu- but it got s- so hard and th- then-"
    h_bethany "Ok, ok, here's what we'll do," 
    
    show h_bethany a_3
    
    h_bethany "we'll get a cup of tea, unpack, get some shopping and then you're gonna sit and tell us all about it. Sound good?"
    "I nod my head as best I can against her, she has no idea just how good that actually sounds."
    
    scene h_asset sorrow with dissolve
    
    "Six PM."
    "Bethany was still at the shop and Paul had some errands he needed to do before going back to work, meaning that once again, I was alone."
    "I flick the tv off and look around the dark room, from nowhere a sudden rush of emotion hits me like a brick and I feel myself starting to panic. Bethany and Paul will be back soon I tell myself, they don't need to see me in this state."
    "In a desperate attempt to combat the feeling of my chest compressing as despair starts to seep through my core, I switch on the lamp next to me and try to get my breathing to steady."
    
    scene bg sadie livingroom day with fade
    show h_holly b_9 at center:
        xalign 0.2
        linear 0.5 faceright
        linear 1.5 xalign 0.8
        linear 0.5 faceleft
        linear 1.5 xalign 0.2
        repeat 10
    
    "I jump up from the sofa and begin pacing the room, repeatedly counting to thirty and back down to one as I walk...it isn't working...my chest won't loosen up...I feel the pins and needles starting in my fingertips...tears start to form in my eyes..."
    
    show h_holly b_9 at center, faceleft with move
    show h_holly b_9:
        yalign 2.0
        xalign 0.5
    
    image bg sadie livingroom cold = im.MatrixColor('images/bg/sadie livingroom day.png', colder(0.7))
    
    "I abandon my pacing on sit hugging my knees on the floor under the window, the cool breeze tickling my cheeks as tears start to drip down them. I might be crying again but at least some of the feelings are coming out."
    
    scene bg sadie livingroom cold
    show h_holly b_9:
        faceleft
        yalign 2.0
        xalign 0.5    
    
    "I don't know how long I've been sitting there but the sound of the front door closing and a heavy object hitting the floor draws me out of my revere. A pair of strong hands grip my arms and I find myself being pulled to my feet and into a welcoming embrace."
    temp_char "Come here sweetheart." 
    "I breathe in deeply as the tears strengthen again"
    temp_char "Sshhhh, it's OK, I've got you."
    "My arms tighten around the warm, soft yet toned body I'm holding without me even bothering to take in who it is, one hand presses against my small of my back while another comes the back of my head and strokes my hair comfortingly."
    temp_char "Sshhhh, just breathe, that's it."
    "The smell of women's perfume starts to seep into my nostrils as the tears slowly begin to stop, I take another deep breath and redouble my grip on the woman holding me, my fingers delving into damp material of her jacket."
    "The fingers running through my hair pause slightly at this and a pair of lips press gently against my forehead."
    
    show h_holly b_8
    
    temp_char "Are you feeling better?"
    
    show h_holly b_8 at faceright
    show h_haley a_7 at centerright with alpha_transition
    
    "I freeze as the sudden realization of who I'm holding onto so tightly becomes clear."
    h_haley "Holly?" 
    "Haley pulls away and looks down at me"
    h_haley "Are you OK?"
    holly "I...erm...I-"
    
    scene bg sadie livingroom day
    show h_holly b_8:
        faceright
        yalign 2.0
        xalign 0.5  
    show h_haley a_7 at centerright
    with dissolve_quick
    show paul a_0 at right, faceleft with easeinright
    
    "The front door opens again and Paul walks in shaking the rain out of his hair."
    paul "Hey guys, everything OK?"
    
    show h_haley a_12

    h_haley "I think Holly could do with some love."
    "Gently extracting herself from my grip and allowing Paul to take over."
    
    show paul a_1 at centerleft, faceright with move
    show h_haley a_10
 
    "No sooner have Haley's arms left my body than Paul takes over, I catch a brief glimpse of her face as he pulls me in, if I'd blinked I would've missed it, but I swear her expression was momentarily pained as she watched Paul hug me...as though she felt aggrieved to see someone else in his arms..."
   
    show h_haley a_12
    
    h_haley "I'm gonna go get us some dinner, I'm feeling Chinese...be back in a bit."
    paul "You want some money?" 
    "He said whilst reaching for his wallet."
    h_haley "No I got it, my treat."
    paul "You should take a brolly, it chucking it do-" 
    
    #door sound
    hide h_haley a_12 with easeoutright
    
    paul "Haley?"

    show h_holly b_8 at faceleft

    holly "I'm so sick of feeling like this."
    paul "It'll pass Holly, we're all here for you, me, Nat, Haley, Blaire...your folks, you'll get through this. I promise."
    holly "Everything feels so dark and lonely Paul," 
    "I sniff against his chest" 
    holly "I know you guys are here and believe me, it means the world, it sounds daft but I just want someone to hold me and kiss me and tell me everything will be alright."
    #mockexpression
    paul "I can and do already do that for you."
    holly "I know you do, but I mean, like...I wish someone loved me the way you love Bethany."
    paul "Hey,"  
    "he pushes me away from him slightly and looks down at me, his hands firmly gripping my shoulders"
    "Somewhere out there, there's some amazing, gorgeous woman desperately searching for you, and I have every faith that one day she'll find you." 
    
    show paul a_7

    paul "And you know I love you...I mean, if you weren't a lesbian and practically my sister, I'd have tried it on with you ages ago."
    
    show h_holly b_10

    "I giggle and tighten my grip around him"
    holly "You did try it on with me remember? You were absolutely convinced that as the captain of the school rugby team you could turn the gay girl...and instead took a slap in the face and a kick between th-"
    paul "And we've been friends ever since. Come on, let's get some stuff ready for dinner."
    
    scene bg connie kitchen day 
    show h_holly b_0 at left
    with fade
    
    "..."
    
    show h_haley b_8 at right with easeinright
    
    "Haley came home roughly an hour later, she was miserable and wet but her arms were full of a welcoming bag of warm food. She was soaked to the skin, her brunette hair, darkened by the rain, stuck in clumps to her forehead and water dripped off the end of her nose as she deposited the bag on the kitchen side and tried to unzip her jacket."
    holly "You should get a shower,"  
  
    hide h_holly
    show h_holly b_0 at left
    show h_holly b_0 at Position(xpos = (placement_of(h_haley).xpos - 0.15)) with move
   
    "walking over to help her with the zip."
    h_haley "I th- think I will d- do," 
    "her brilliant eyes fixed firmly on my fingers as I pull the zip down and try to prise the sodden material from her skin"
    h_haley "th- thanks."
    
    show h_holly b_1
    
    holly "No problem."
    
    outfit h_haley casual
    show h_haley b_9
    
    "I do a double take and try my best not to drool as I notice for the first time just how incredible her body is. The tank top she's wearing is practically transparent and does nothing to hide the swell of her breasts, the flat stomach or tight abs beneath it."
    holly "It's seriously chucking it down then?" 
    "My fingers absentmindedly reaching out to press lightly against her stomach."
    h_haley "Yeah." 
    "her eyes meet mine before dropping down to the hand against her body."
    "I quickly retract my hand and turn back to the food, a light blush spreading across my cheeks."
    
    show h_holly blush b_2
    
    paul "We'll wait for you Haley," 
    "Paul says, thankfully noticing nothing," 
    paul "Beth will be here in ten minutes so we can all eat together."
    h_haley "That's gr- great," 

    show h_haley b_7

    h_haley "I'll try and be quick."

    scene bg sadie livingroom day with dissolve:
        zoom 2
        xalign 0.93
        ypos -0.7
    show h_holly b_0 at center, faceleft
    outfit h_haley casual_b
    show h_haley a_0 at centerright
    show h_bethany a_0 at centerleft, faceright
    show paul a_0 at right, faceleft
    "It wasn't long before the four of us were sat together eating dinner and watching a movie on TV. Haley had brought a selection of different things from the Chinese, including all of my favorites, but I was so exhausted I was struggling to keep my eyes open, let alone get food into my mouth. I only lasted twenty minutes before announcing I needed to go to bed."
    paul "You sure pal?"
    h_bethany b_0 "You've hardly eaten a thing Holly, are you feeling OK?"
    holly "I'm fine, I'm just tired...didn't sleep much last night. If I'm hungry later I'll come back for this," 
    "I indicate my plate"
    holly "Night guys."

    hide h_holly with easeoutleft

    "I drop my plate in the kitchen and head straight to my room, I thought it'd be an age before I fell asleep but as soon as my head hit the pillows I was out."
  
    scene bg connie bedroom clean dark with swirl_transition
    
    temp_char "Holly! Holly? Wake up!"
    "My eyes fly open and I find Haley sitting beside me on the bed, her expression anxious. Without pausing she sits back and pulls me with her, wrapping my arms around her waist and holding my head against her chest."
   
    outfit h_haley robe
    show h_haley a_7 at centerleft, faceleft with dissolve_quick
  
    h_haley "Try to breathe...that's it sweetheart...it was just a dream. You're OK, I'm here."
   
    with hpunch
    with vpunch
   
    "My body shakes uncontrollably as I try to calm down, I'm absolutely soaked through with sweat, my sheets even feel damp beneath me. I don't know what I was dreaming about but judging by the state I'm in, it wasn't something nice."
    "Haley keeps up a constant stream of encouragement and words of comfort as we sit there, the rhythmic beating of her heart and focusing on her voice helps me to come around and I slowly manage to get myself back under control."
    holly "Thank you." 
    "I whisper, my voice thankfully not wavering too much as I speak."
    h_haley a_12 "Don't even mention it." 
    holly "Where's Paul?" 
    "Her heart beats a little stronger against her ribs at the mention of his name and I wonder again if perhaps she likes him."
    h_haley a_13 "He went out for a drink with Bethany."
    holly "And you got stuck babysitting, right?"
    h_haley a_12 "Actually, I didn't fancy being the third wheel for the evening," 
    "Reaching up and tying her long hair into a ponytail - PRETEND AT LEAST I CAN'T BE ASKED PSING IT"
    h_haley "I'd much rather be here."
    holly "You're not seeing Dominic?"
    h_haley a_10 "Definitely not." 
    holly "I'm sorry." 
    holly "I don't mean to sound ungrateful...I just don-"
    h_haley a_12 "It's OK Holly, I promise you no-one wants you to feel like we're babysitting you. We just want to help get you back to normal again."
    "An uncomfortable silence follows this."
    h_haley "Tell you what," 
    "Haley says loudly, breaking the tension,"
    h_haley a_7 "Why don't you get a shower and put some dry clothes on? Are you hungry, I could warm that Chinese up for you?"
    holly "Th...tha..that sssss-ounds amazing." 
    "I'm not hungry, but the worried look on her face hasn't faltered since I woke up to find her sitting with me."
    h_haley "Great." 
    
    outfit h_holly bikini
    show h_holly b_8 at left, faceright
    
    "Her smile widens as she unwraps her arms from around me and heads towards the kitchen."
    
    hide h_haley with easeoutright
    
    "Shaking my head, I stagger to the bathroom and pull my wet clothes off before jumping in the shower, the hot water feels amazing against my skin and energises me enough that I manage to wash my hair. By the time I'm finished I actually do feel a little hungry."
    
    hide h_holly with easeoutright
    scene bg connie kitchen day with dissolve
    outfit h_holly casual_b
    show h_haley a_12 at left, faceright 
    show h_holly b_0 at right, faceleft with easeinright
   
    holly "Erm, Haley? Why are my sheets here?"
    h_haley blush a_13 "Oh, well...they were kind of soaked through...so I thought I'd get them in the wash for you."
  
    show h_holly b_8 at centerleft with move
   
    "I sit down at the table and she hands me a streaming plate of food."
    h_haley "Your mattress is kind of soaked through too...it's OK though," 
    "she adds hastily on seeing my face,"
    h_haley "you can sleep in my room, I'll sleep out here."
    holly "You don't have to do that," 
    "I shake my head and push some food around my plate,"
    holly "I probably won't sleep much more tonight anyway."
    h_haley "Holly you need to sleep." 
    "I shake my head again"
    holly "I can't Haley, once I'm awake that's it...I'll be OK." 
    "I put a forkful of food into my mouth and chew slowly as a gesture of goodwill, but she isn't fooled."
    h_haley a_6 "How about this, you get in my bed and try to sleep, I'll sit with you all night so if anything happens you aren't alone...and if that doesn't work, you're free to stay awake all night to your hearts content and I won't mention it ever again?"
    "I tentatively try another mouthful of rice and consider her offer."
    holly "Aren't you at work tomorrow?"
    h_haley "Nope."
    holly "I don't know..."
    h_haley a_5 "Please?"
    "I draw my gaze away from my food and meet her eyes, she looks genuinely concerned."
    holly "OK." 
    "I mumble quietly, staring at my plate once again as my desire to eat leaves me."
    h_haley "Did I get your favorites wrong?"
    holly "Hmmm?" 
    "I look up."
    h_haley a_2 "The food, I was sure I'd got your favourites?" 
    "She frowns a little, as if she's trying to remember something she forgot."
    holly "No, you did a great job, all my favorites," 
    
    show h_holly b_1   

    "I'm just...tired...I guess."
    h_haley "Bed?"
    "I can only nod in agreement as I tip the food into the bin and put my plate in the sink."
    
    hide h_holly
    hide h_haley
    with easeoutright
    scene bg leona room dark with fade
    show h_holly b_0 at left
    show h_haley a_7 at centerleft
    with easeinright
  
    "I follow Haley to her room and climb into bed as she holds the covers open for me, with a little encouragement I lay back against the pillows and take a deep breath. She settles into the chair next to her bed."
    h_haley "Ok, now I'm right here, no-one is getting in without going through me first," 

    show h_haley a_14

    "She gives me a toothy grin I can't help but return" 

    show h_holly b_10

    h_haley "so lay back, close your eyes and try to drift off."
    "I laugh a little and turn onto my side facing her, stifling a yawn as I realize just how exhausted I actually am."
    h_holly b_2 "Thanks Sweetie." 

    show h_holly b_1

    h_haley "Sweetie, eh?"
    "I see the brief glimmer of a huge smile etched on her face before my eyelids close completely and I drift off."

    show h_haley b_9 at faceleft
    with Fade(0.5, 0.7, 0.5)

    show h_haley b_9 at faceleft
    show h_holly b_4

    "The time on the alarm reads 3:15am, I can't believe I've managed to sleep until now, a whole five hours! I look across at Haley, asleep, but still in her chair, just like she promised. I feel a pang of guilt when I note just how uncomfortable she looks, I shuffle slightly and her eyes open instantly."
    h_haley b_8 "You ok?" 
    "She croaks before clearing her throat." 
    "I nod"
    holly "You look really uncomfortable there."
    h_haley "I'm fine, I've slept in worse places...and you're my main concern at the moment."
    holly "And you're doing a great job of taking care of me, but I feel horrible looking at you scrunched up in that chair...especially when this is actually your bed."
    h_haley"It's honestly fine Holly..." 
    
    show h_haley at right,faceright with move
    
    "She stands and stretches, wandering over to the window and opening it slightly"
    h_haley "it's still throwing it down out there."
    
    show h_holly at Position(xpos = (placement_of(h_haley).xpos - 0.10)) with move
    
    "I climb out of bed and move over to join her; a pleasant shiver passes through my body as the sound of rain reaches my ears and I find myself leaning into Haley a little."
    holly "Please get in bed, it doesn't feel right me being in there and not you...I'm happy to share if you are?"

    show h_haley b_2

    "She looks over at the bed and bites her lip softly, as though she's weighing up a huge decision."
    holly "Please Haley..." 
    "I beg. I may have only called her Haley once before, but the reaction I got was enough to tell me that that was how to get her to be more agreeable."
    h_haley b_11 "Ok." 
    "She sighs eventually, the smile I predicted playing on her lips."
    
    show h_holly at left
    show h_haley at Position(xpos = (placement_of(h_holly).xpos - 0.10))
    with move
    
    show h_holly b_1
    show h_haley b_9

    "I smile and climb back into bed, the mattress sinks down when Haley crawls in beside me, but other than that she barely makes a sound. I reach out and switch off the lamp, the sound of the rain outside and Haley's light breathing quickly lulling me back to sleep."
    
    title "The Bottom"
    scene bg leona room day shut

    "I wake the next morning to find myself snuggled closely into a pillow in the middle of the bed. Oh god...I must've rolled over in the night and tried to cuddle Haley...I grimace at the thought...she must have put the pillow here to stop me..."
    "I drag myself out of bed with the intention of getting some warmer clothes on and maybe going for a walk but as soon as I look out the window I rapidly change my mind; the rain is still coming down in sheets."
    "Instead I wander back to my room and freeze in the doorway...Haley is bent over my bed pulling a sheet into place...how is it that I've never noticed how nice her bum is before?"

    scene bg connie bedroom clean day with dissolve_quick
    show h_haley b_11 at left, faceleft
    show h_holly b_4 at right, faceleft with easeinright

    h_haley "Morning Holly," 
    "She says without looking at me" 
    
    show h_haley b_15 at faceright

    h_haley "How're you feeling today?"
    holly "Oh, erm," 
    "I start, tearing my gaze away from my new favorite view" 
    holly "A lot better actually."
    "I walk around her and pull some clothes out of my wardrobe."
    holly "Thank you...for last night...I really appreciate it." 
    "I fiddle absentmindedly with my sleeve."
    h_holly b_1 "I haven't slept that well for weeks...and thanks for making my bed too."
    h_haley "You're more than welcome."

    show h_haley b_16 at Position(xpos = (placement_of(h_holly).xpos - 0.10)) with move

    h_haley "Want to go for a walk in the rain?"
    holly "It's worse than last night out there. We'll get soaked."
    h_haley "So?"
    holly "So, we'll get soaked."
    h_haley "It'll be fine. We'll take that huge umbrella I borrowed from work."

    show h_holly a_1

    "I'm not convinced...but I smile and allow her to drag me from the house ten minutes later under the enormous umbrella she took from work."

    hide h_holly
    hide h_haley
    with easeoutright

    scene bg sadie livingroom day with fade
    show h_bethany a_0:
        zoom 0.5
        yalign 0.7
        xalign 0.75
        faceright
    show paul a_0:
        zoom 0.5
        yalign 0.7
        xalign 0.85
        faceleft
    pause 0.0

    show h_haley b_7 at center, faceleft
    show h_holly b_4 at centerleft, faceright
    with easeinright

    h_bethany a_3 "Where the hell have you two been?"
    "Bethany laughs, looking up from the TV."
    h_haley "I thought Holly could use some fresh air." 
    paul a_5 "And get pneumonia in the process!" 
    "Paul interjects, his voice suddenly harsh."
    holly "I can take a bit of weather Paul."
    paul "That's not the point! We're meant to be taking care of you...not getting you even more sick!"
    "Sick? They think I'm sick?"

    show h_bethany a_6

    h_haley a_3 "She's fine Paul." 
    
    show h_holly b_8

    holly "You think I'm sick?" 
    "Haley & Bethany" "Of course not!" 
    "They both shrieked together"
    holly "What about you?" 
    "I ask Paul, my voice barely above a whisper" 
    holly "Do you think I'm sick? That I need babysitting constantly in case I have a breakdown? That I'm so fragile I can't handle even the simplest task?"
    paul "If you could handle the simplest task you wouldn't be in the state you are now!"
    "He screams the last words"
    
    show h_holly a_4
    
    holly "If you hadn't tried so hard to push Erin on me when I clearly wasn't interested I wouldn't be in the state I'm in now!!!"
    "He opens his mouth to speak but instead of the apology and words of comfort I was expecting he says nothing, just sits there looking at me, his eyes piercing and cold. A devastating silence fills the room, I can't believe we've reached this stage, I look at Paul, my best friend, my partner in crime, my soul confidant over the years and suddenly I don't even recognize him anymore."
    
    show h_holly b_9
    
    "Tears fill my eyes, I don't know where to go, or what to do, I push past Haley on my way out the door and head back out into the rain."
    
    show h_holly b_9 at right with move
    show h_haley a_7 at faceright

    h_haley "Holly-"  
    "She reaches out a hand to try and stop me."
    
    hide h_holly with easeoutright
    
    "I ignore her and carry on, leaving without picking up the umbrella. Once outside I simply just start walking as fast as I can, not paying attention to where I'm going or who I'm walking in to."

    scene h_bg cloud
    show h_asset rainabove

    "My vision blurs as a combination of tears and rain drops drip down my face, I can't get over Paul's reaction. I turn the corner into the park and crouch down under the nearest tree, this doesn't do much to keep the rain off me but at least provides a little shelter from the wind."
    "I lean back against the tree and try to ignore the whirlwind of thoughts now flying through my brain, instead I hold out one hand and focus on the steady drip of water falling from it onto the ground underneath. How could he say those things? He's supposed to be my best friend..."

    #longfade
    scene h_bg cloud_dark with Fade(0.5, 0.7, 0.5)
    show h_asset rainabove

    "When I next take stock of reality it's almost dark, my clothes are so wet they fit like a second skin and rise up my arms and legs as I stand. I wince as blood flows back to my outer limbs and begin to stagger home..."
    "By the time I arrive back at home I can't even feel my fingers and opening the door is next to impossible. I give up after only a few seconds of trying and land a feeble knock on the wood. The door opens instantly to reveal a relieved looking Haley half way into pulling on her coat."

    scene bg sadie livingroom day
    outfit h_haley coat
    show h_haley a_7 at centerright, faceright
    show h_holly b_7 at right, faceleft with easeinright

    h_haley "Holly!"
    "She exclaims, wrapping her arms around me tightly"
    h_haley "Thank god you're home! I was just on my way out to find you. I've been so worried!"

    show h_holly b_8 at left with move
   
    "I don't answer, I know she means well, I know she's just trying to help, but suddenly I find I'm so angry with her I can barely stand to be in her presence. I roughly push her away and head for the bathroom."
    h_haley "Holly?" 
   
    show h_holly b_2 at faceright
   
    "I raise my eyes to look at her, one arm still in her coat as she slips her shoes off."
    "{b}Just don't Haley, I'm too tired, I don't wanna hear it!{/b}"
    
    show h_haley a_9 at Position(xpos = (placement_of(h_holly).xpos + 0.10))
   
    h_haley "Hey!" 
    
    show h_holly b_8 at faceleft
    
    "She grabs my hand as I turn to walk away."
    holly "I said don't!" 
    "My voice rising to a shout"
    holly "I know you all think I'm pathetic and feeble but I'm capable of getting myself a shower!"
    h_haley "We don't think that, we-"

    show h_holly a_4
    
    holly "Are you fucking deaf?!" 
    "I scream manically."
    show h_haley b_0
    holly "Just leave me the fuck alone! I don't need your fucking help or your pity!"

    hide h_holly with easeoutleft
    scene bg rachel bathroom with swirl_transition
    show h_holly b_9 at left, faceright
   
    "At last, in the bathroom. But my fingers are still so numb I can't get the door locked. I also can't get out of my clothes, the harder I try the more frustrated and upset I get. Soon the tears are flowing again and my loud sobs echo off the tiles around me as I slide to the floor."
    h_haley "Holly?" 
    "A tentative voice enquires from the other side of the door"
    h_haley "Can I come in? Please."
    "OK... *sniff*"
    
    outfit h_haley casual 
    show h_haley a_7 at left, faceright
    show h_holly b_9 at centerleft, faceleft
    with move
    
    "Slowly the door opens and Haley slides into the room. She says nothing. She pulls me easily to my feet, helping me to pull my arms out of the top, and t-shirt follow soon after. Still without speaking she turns on the shower before helping me out of my jeans, leaving me standing there in my underwear."
    
    outfit h_holly bikini 
    with dissolve_quick
    
    h_haley "Can you do the rest?"
    holly "I can't undo my bra." 
    "I cry pathetically as I try to lift my arms."
    
    show h_haley a_7 at center, faceleft
    
    "To her credit she simply walks around me and helps me to remove the fiddly item, then she encourages me into the hot water. My skin feels like it's on fire as the water hits."
    h_haley "It's only luke warm, I promise."
    "She sits on the side of the bath."
   
    "As the pins and needles slowly ease off I manage to slip my panties down my legs, I look over sheepishly at Haley but find she's looking the other way to give me at least some privacy. I struggle through washing myself with arms that feel like lead before switching off the water and stepping out of the shower."
    
    outfit h_holly nude 
    with dissolve_quick

    "Haley stands and wraps me a large fluffy towel, rubbing my arms to try to get the blood pumping better."
    holly "I'm so sorry Haley..." 
    holly "I don't deserve this kindness. *Sniff*"
    h_haley "It's ok." 
    "She replies as she continues to help me get dry, deliberately avoiding any particularly sensitive areas."
    holly "{i}It's not.{/i}" 
    h_haley "Holly, it's fine, I get it." 

    show h_haley b_11 

    h_haley "Can you finish up here?"
    "I nod and shuffle the towel around taking in Haley's eyes wandering over my body before she leaves the room to allow me to finish."

    hide h_haley
    hide h_holly 
    with easeoutleft
    scene bg connie kitchen night
    show h_holly b_8 at left
    show h_haley a_7 at centerleft

    "I leave the room with the intention of going to bed but Haley has other ideas, she drags me to the kitchen and puts a plate of food and a cup of tea in front of me, instructing me that I'm not leaving her sight until it's gone."
    "It takes me well over an hour to finish it, but she sits patiently by my side until I'm done."
    h_haley "Right," 
    "she says taking the plate and cup from in front of me"
    h_haley "You're free to do as you please now, I just wanted to make sure you ate."
    holly "{i}Thanks.{/i}"
    

    #-----------------------------------------------------------------------------------------------------------------
    #Position(xpos = (placement_of(h_holly).xpos - 0.10)) with move

    scene h_asset sorrow
    scene h_bg star
    scene h_bg day
    scene h_bg dusk
    scene h_bg cloud
    scene bg connie bedroom clean night
    scene bg connie kitchen day #/ night / evening
    scene bg sadie livingroom day 
    scene bg sadie livingroom day blur
    scene bg connie bedroom clean dark
    scene bg connie bedroom blur
    scene bg leona room dark
    scene bg rachel bathroom
    #Lower xalign -> more to left
    #Lower ypos -> downwards
    placeholder
    show h_asset glass_1
    pause 0.05
    show h_asset glass_2
    pause 0.05
    show h_asset glass_3
    pause 0.05
    show h_asset glass_4
    pause 0.05
    show h_asset glass_5
    pause 0.05
    show h_asset glass_6
    pause 0.05 
    show h_asset glass_7
    pause 0.05
    hide h_asset glass_7 with dissolve
    show white as flash:
        additive_flash(0.1)

    #Livingroom sofa
    show h_holly b_9:
        zoom 0.5
        yalign 0.7
        xalign 0.75
        faceright