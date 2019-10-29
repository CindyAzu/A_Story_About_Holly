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
    "I'm actually not sure what to do now, I feel lost again without something to focus on or someone telling me what to do. I look aimlessly around the room trying to find inspiration, but all I can focus on is Haley stood at the sink washing up. A fresh wave of guilt washes over me as I watch her, she's been nothing but kind to me, taken better care of me than anyone else and yet she's the one I've sworn at and shouted at..."
    show h_holly at Position(xpos = placement_of(h_haley).xpos - 0.15) with move
    "I stand up and walk across to her, pulling her hands out of the soapy water to give her the biggest hug my numb arms can manage."
    holly "I'm sorry Haley, there's no way you deserve the way I've treated you this evening. You've been nothing but kind to me and I've been an ungrateful bitch."
    h_haley "It's OK Holly," 
    "she whispers, the water from her hands and forearms soaking through my hoodie as she holds me tighter"
    h_haley "You've been through a lot the past few days. All I want is for you to feel better."
    holly "I don't understand why you care so much, you hardly know me. I should be the least of your worries."
    h_haley "Well I...I just...we're friends aren't we? You should take care of your friends." 
    "She pushes me away gently and I notice her cheeks look flushed"
    h_haley "Let me finish up here and we'll watch a movie or something OK?"
    holly "OK." 
    "I nod."
    
    scene bg sadie livingroom day with fade
    show h_holly b_2 at centerright, faceright with easeinleft
    
    "I wander into the front room but change my mind when I realise that there's a good chance I'll have to see Paul at some point. I turn around to backtrack into the kitchen and walk straight into Haley coming the other way."
    
    hide h_holly b_2 at faceleft with easeoutleft
    scene bg sadie livingroom day blur 
    
    h_haley "Changed your mind?" 
    "She smiles"
    holly "No," 
    "I smile back," 
    holly "but can we watch somewhere else? I don't want to see Paul." 
    h_haley "No problem, go get settled in my room and we'll watch in there, any preferences?" 
    "I shake my head" 
    holly "Paranormal Activity?"
    h_haley "Definitely not...unless you fancy spending the night with me clinging to you."
    holly "I could think of worse things." 
    "She grins and tilts her head suggestively at me...I say nothing, unable to decide if she's joking or not" 
    h_haley "How about Despicable Me then?" 
    "She continues when I remain silent."
    holly "Sounds good." 
    #holly sleeping
    scene bg leona room dark
    show h_holly b_2 at left
    show h_haley a_13 at centerleft

    "Ten minutes later we're laid together under the covers on Haley's bed in an uncomfortable silence, I shuffle down and rest my head on the pillows...a fatal mistake as my eyes instantly start to close."
    "I jerk awake only five minutes later to find Haley looking down at me."
    holly "Sorry." 
    "I mumble sheepishly."
    "She pulls my pillow into her side and encourages me to lay down again" 
    h_haley "Rest your head here." 
    "She pats the pillow and I slowly lay down."
    #haley expression 
    "Her expression is unfathomable while I adjust my position and try to get comfy, but as soon as she deems I'm sorted, what's bothering her becomes clear quickly."
    h_haley "Is this the worst it's been?" 
    "Looking anxiously down at me as she brushes her fingers through my hair."
    "I pause for a few seconds and contemplate my answer. Shaking my head slowly, I take a deep breath and reveal what I've never told another soul."
    holly "I thought about suicide once..."
    h_haley "Oh Holly." 
    "Haley gasps and gives me a worried look" 
    h_haley "When?"
    holly "Before I started seeing Blaire." 
    holly "I was driving home after a shit day at work, my anxiety was through the roof. Then I got to the road by the river and suddenly all I wanted to do was just drive off the edge and into it, it would've been so easy." 
    "I pause slightly"
    holly "In fact, for those few seconds, when I had that thought, I felt at peace somehow, you know? The anxiety was gone, it faded away instantly, as though my mind knew that that was the answer..."
    h_haley "What stopped you?" 
    "She asks quietly, her fingers still tangled in my hair."
    "I realized it was a blind bend and I was on the wrong side of the road. I didn't want to risk hurting someone coming the other way when I flew off the edge. Taking my own life would've been one thing, but the idea of taking out someone completely innocent was a whole different ball game...and I decided that I really didn't want to die..."
    #haley expression tears??
    "I look up at Haley and see her eyes welling with tears."
    holly "Hey," 
    "I sit up, wrapping my arm around her shoulders" 
    holly "It's OK, I'm not there anymore, no one got hurt and I only thought about it once...it was actually that thought that made me decide to get help."
    h_haley "Why didn't you tell anyone Holly?" 
    "Her hands shaking a little as she wipes her eyes" 
    h_haley "I knew you'd been down but I had no idea it was that bad."
    holly "I don't know." 
    "I shrug, wishing I hadn't admitted anything" 
    holly "I've just never thought of it as something anyone else needed to know...and now I'm getting help, worrying about it seemed pointless."
    #haley tears?
    "Her eyes well up again and tears drip down her cheeks."
    holly "Don't cry Haley" 
    "I pull her in for a hug and her arms wrap tightly around me" 
    holly"I'm not worth crying over, there are bigger problems in the world."
    h_haley "You always say things like that Holly," 
    "she sniffs and looks up at me, her eyes staring straight into mine" 
    h_haley "There might be other problems out there, but you are definitely worth crying over. In fact, you're worth so much more than crying over! Do you have any idea how much hurt anyone who knows you would've felt if you'd gone through with it? Everyone who meets you loves you sweetheart, and those lucky few that are allowed into your world, that get the chance to get close to you, they think you're incredible, they'd do anything to make you happy, they just adore you Holly." 
    "She takes in a deep breath to steady herself, the tears fall thick and fast down her cheeks now."
    h_haley "You're so kind and considerate, I can't believe that even in that situation your first thought was that you might hurt someone else. And you're so strong, you don't give yourself nearly enough credit for getting through what you have, depression is a seriously difficult thing to overcome and you fight yourself at every turn, I've seen you do it. Letting people into your world is hard, even harder after what happened with Erin..."
    h_haley "I just want you to know that you're not alone in this Holly, we're all here for you and we all want the best for you because that's all you want for everyone else. I hope so much that one day you get your happy ending sweetheart; I've never met anyone who deserves it more than you."
    "She takes another deep breath and rests her head against my chest, trying to get her breathing back to normal. I don't know what to say, I pull her in closer and lean against the headboard, kissing the top of her head softly as I run my fingers across her back."
    holly "This makes me happy," 
    "I whisper" 
    holly "I'm so glad to have you in my life Haley."
    h_haley "I want you to promise me something." 
    "her voice muffled by my hoodie."
    holly "What?"
    h_haley "I want you to promise that if things ever get that bad again, you'll come find me and tell me...or call me, or text, or write a letter, or...or...just promise me you won't suffer alone."
    holly "I promise." 
    "I answer earnestly." 
    h_haley "Good."
    "Her fingers grip my hoodie tightly as fatigue starts to stab at my eyes."
    h_haley "It's OK Holly, go to sleep." 
    "She whispers, obviously able to feel my breathing deepening and my body relaxing under her."
    holly "Thanks Haley."
    "I sigh as I drift off once more."
    with fade
    #Sleepy time add sleepy expression mby drool?

    "My eyelids flutter open again in the early hours of the morning. I've shuffled down into the bed in my sleep and Haley is now laid beside me, the pillow still separates us but her fingers are entwined in my hair. I smile a little at this comforting gesture and adjust the pillow so I can shuffle closer to her. She sighs and closes the gap between us fully, her hand drops to my waist and she pulls me gently into her body until my forehead is touching her chin."    
    "Her lips press softly against my skin and I wrap my arm around her before sleep consumes me once again."
    with fade
    #scene morning
    "I wake the next morning to Haley attempting to slide out of bed without disturbing me, a difficult feat as we're still wrapped so closely around each other it's hard to tell which limbs belong to each of us."
    h_haley "Morning," 
    #haley smile 
    "How're you feeling?"
    holly "Like I've got one hell of a cold coming on," 
    "I groan as I take note of the pounding headache, sore throat and blocked nose I've woken up with"
    holly "I'm definitely going to suffer for yesterday."
    h_haley "Stay here and try to go back to sleep," 
    "She smiles again and throws a blanket over the bed" 
    h_haley "I'll come and check on you in a bit." 
    "She tucks some stray hairs behind my ear and leaves."
    "A warm, fuzzy feeling fills my chest as I snuggle back down under the covers and manage to fall into a thankfully dreamless sleep."
    #haley disapear
    scene bg sadie livingroom day with dissolve
    show h_holly b_0 at centerleft, faceright with easeinleft
    show h_haley a_13 at centerright faceleft

    "I wander into the front room some three hours later."
    h_haley "Hey sleepyhead," 
    "Haley grins as I slump down next to her on the sofa" 
    h_haley "Sleep well?"
    holly "Better than I have done in weeks." 
    #holly smile
    holly "Thank you so much Haley, I don't know what I'd do without you."
    "She pulls me in for another amazing cuddle that warms my soul and eases the throbbing headache I'm still experiencing."
    h_haley "I've got some good news for you..."
    holly "Hmmm?" 
    #holly close eyes
    #haley concerned
    h_haley "Bethany messaged to say her and Paul were going away for another few days." 
    "My eyes snap open" 
    h_haley "She thought...and I agree...that maybe it'd be good for you and Paul to have a bit more of a break from each other..."
    holly "Maybe..." 
    #cuddles?
    h_haley "Space might be just what the two of you need." 
    "She kisses my forehead" 
    h_haley "But you know... I don't think what he said came from a malicious place..."
    #holly mad
    holly "It sounded pretty malicious to me."
    h_haley "I know, but I think he just panicked, I don't think he really understands-"
    #holly even more mad
    holly "That doesn't give him the right to say what he did." 
    "I reply angrily, wondering why she's trying so hard to defend him."
    h_haley "I know." 
    "She kisses my forehead again and changes tact."
    h_haley "So I was thinking...it might be a bit soon for you to go back to work, but how about we try going to the shops this afternoon? We could get something for dinner, maybe cook together, then watch a film before bed?"  
    holly "{i}Sounds good.{/i}" 
    "Privately I think it sounds awful, I know she's only trying to help me get better and distract me from my thoughts, but right now all I want to do is curl up on the sofa with her arms wrapped around me and not move for a considerable period of time."
    #scene swap? blur?
    scene h_bg dusk with dissolve 
    
    "Overall the shopping trip went well, I only had a few moments of panic as we went up and down the aisles, but Haley did an amazing job of keeping me calm and distracted. We got home, put the food away and made a basic meal of spaghetti before settling down to watch the film."
    
    scene bg sadie livingroom

    "The closer we got to it being time to go to bed, the more despondent and withdrawn I became. I knew Haley would be heading out to work in the morning and that she'd need a full night's sleep, she couldn't sit up talking to me..."
    h_haley "You ok sweetheart?" 
    holly "What? Oh...yeah I'm fine." 
    h_haley "Talk to me Holly,"
    " she pauses the TV" 
    h_haley "You can't get better if you keep everything inside."
    holly "It's really stupid..."
    h_haley "I won't laugh, I promise." 
    #extra smile haley
    "She smiles and lifts my chin." 
    holly "I really don't want to go to bed..." 
    "I breathe"
    "it's like...I can get in bed and fall asleep, but I can't stay asleep and then my mind starts working overtime thinking about nothing...and then I either fall asleep again and have a nightmare...or I wake up every ten minutes feeling anxious and like the walls are closing in in the dark..." 
    "I pause for breath" 
    holly "And I also really don't want to wake you up in the early hours if I have another bad dream when I know you've got to get up for work..."
    h_haley "Ok"
    # haley mega smile
    h_haley "first of all, I appreciate your concern over waking me, but honestly I'd much rather you did than struggling on in the dark feeling like that. Secondly, that's not stupid at all! You need to give yourself more credit, you've been through so much recently, I'm surprised you're even managing a bit of sleep...and finally," 
    "she pulls me in for a hug" 
    "If you ever feel like you just can't cope alone, please come and wake me up."
    "I nod with as much conviction as I can and tighten my grip around her waist."
    h_haley "I'm gonna grab a quick shower and then get in bed," 
    "She says and I loosen my grip," 
    "if you need anything...and I mean anything...you come and see me, OK?"
    holly "OK." 
    #holly smile
    "As Haley leaves I figure I may as well try and get myself to sleep, I feel tired even though I've actually slept for most of the day."
    "I sigh loudly as I stand up and switch off the tv. A quiet determination fills my brain and I take several deep breaths...I will not wake Haley up later."
    #transition to night room
    with fade
    #holly cry
    "I wake up in a cold sweat...looking across at the clock I'm almost heartbroken to find it's only 2:38am. The familiar feelings of panic and anxiety begin to filter through my body before I even have chance to stop them."
    "I close my eyes and try to get a handle on my breathing, in through the nose, out through the mouth, all that crap. Needless to say, it doesn't work. I finally give in and leave the room with the intention of getting a drink from the kitchen and going to sit in the front room with something random on the TV in an attempt to feel like I'm not alone."
    "I get halfway down the hallway and pause outside Haley's room. My hand hovers over the door handle and I bite my bottom lip, weighing up my options before deciding that despite what she said, I can't do this to her so early in the morning. I get as far as pulling my hand away when the door opens from the other side."
    #show haleys
    h_haley "Come here sweetheart." 
    "Haley takes my hand and drags me into the room."
    "I don't even try to stop her, I'm so thankful she opened the door I can't even speak. Silent tears run down my face as we climb into bed and she pulls me to her."
    "She lays back and her arms wrap around me as she holds me tightly against her body, I rest my head on her chest and listen to the comforting thump of her heart beating under her ribs."
    holly "I'm sorry," 
    "I whisper when my breathing evens out"
    holly "I really didn't mean to wake you, especially when you've got work in a few hours..."
    h_haley "Hey," 
    "she kisses the top of my head" 
    h_haley "It's OK, I promise, you didn't wake me, I was coming to check on you anyway, you just saved me a few steps."
    "That's a lie and I know it...but I appreciate the sentiment all the same."
    h_haley "I was actually thinking, maybe it'd be better if you just came to bed with me at night? I mean, until you feel you'd be OK by yourself...like...you'd sleep without nightmares and all that."
    "Her heart pounds strongly against her ribs as she proposes this and I can tell she's flustered despite the fact the room is in total darkness."
    holly "What about Dominic?"
    h_haley "He never stays over." 
    "She replies quickly."
    holly "Oh."
    h_haley "Yeah...he likes to leave as soon as he's done...and to be honest I don't want him here afterwards..."
    holly "Do you want him here before?" 
    "I blurt out before I can stop myself."
    h_haley "Not really." 
    h_haley "I think I should just end it."
    holly "Maybe."
    "I nod, tightening my arms around her before speaking again"
    holly "Sharing would be really awesome Haley, thank you."
    #haley hyped 
    h_haley "Great!" 
    "A huge weight feels like it's been lifted as a massive smile spreads across my face...and despite what I try to tell myself, I know I'm smiling at more than just the offer of help with easing the nightmares."
    
    title "Session"
    scene bg corporate lobby small with dissolve
    #show holly + blaire holly crying
    
    holly "I'm sorry," 
    "I manage to get out between sobs" 
    holly "I thought I was past this stage...again..."
    h_kisaragi "It's not a problem Holly, I promise. You need to get your feelings out, and I know how hard you've worked on that, but there's absolutely no shame in crying every once in a while."
    holly "I try so hard to act like things are ok, to keep everything on the surface happy and light, but inside things are so dark and cold and lonely and...and...and kind of numb."
    h_kisaragi "Numb?" 
    holly "Yeah...like, I'm not even sad anymore, it's as though I've gone beyond that and now I just don't feel anything at all."
    h_kisaragi "Do you always feel like this?" 
    #Blaire smile
    holly "When I'm with my friends, or out doing something I used to enjoy things are a little bit better, but then the next day things are exactly as they were before. Except..."
    h_kisaragi "Except?" 
    holly "Except with Haley."
    "I can feel a small smile playing on my lips" 
    holly "I don't know how she does it but she makes me feel...lighter...somehow."
    h_kisaragi "Perhaps that's because you feel you can relax around her...or perhaps you see her as something more than a friend?"
    holly "What? No!" 
    #holly flabergasted with awe?
    holly "She's straight...and a friend...and she still has a boyfriend..."
    h_kisaragi "Ok, ok," 
    "Blaire laughs, raising her hands in surrender"
    h_kisaragi "She's a friend...although I feel we need to push this out at least as far as, she's a 'close' friend."
    holly "Ok." 
    h_kisaragi "Now, as far as homework goes for this week. All I want you to do is simply to keep doing what you're doing." 
    "I look across at her, a little surprised by this"
    h_kisaragi "Everybody has setbacks Holly, but I know that if you keep doing what you were doing before, things will start to become easier...maybe even enjoyable."
    holly "God I hope you're right." 
    "I sigh" 
    holly "I'm exhausted."
    h_kisaragi "Go home and relax,"
    #smile blaire 
    h_kisaragi "Today was a hard session, give yourself a break."
    holly "I will, thanks Blaire."
   
    scene bg connie kitchen night

    "Later that day."
    "I walk through to the kitchen and switch on the kettle, hoping that my eyes look a lot less sore than they did as I got back in the car. The door swings open again and Haley walks through it, toweling her hair dry."
    #show haley easein

    h_haley "I was just about to do that," 
    #haley smile
    h_haley "I thought you'd be back about now and you'd want a drink."
    holly "You don't have to make me drinks,"
    #holly smile 
    holly "you want one?"
    h_haley "No thanks." 
    "She drapes her towel over one of the chairs, revealing my favorite t-shirt and a pair of shorts"
    holly "Oh..." 
    "She grins when she sees where I'm looking" 
    h_haley "I sort of borrowed this...I hope that's OK?"
    holly "It's fine," 
    "I reply light-heartedly, while secretly hoping that she never wears it when she sees Dominic" 
    holly "it's not like I have a girlfriend to steal my clothes, you may as well have the honor."
    h_haley "Don't mind if I do." 
    "She kisses me on the cheek and gives me a quick hug" 
    h_haley "Come cuddle when you're sorted. I want to hear how your session went."
    holly "Yes boss." 
    "I salute." 
    "I catch sight of myself in the window as she leaves and almost don't recognize myself. The woman in my reflection looks...well she looks happy...she's smiling, her eyes don't look sore, in fact, her eyes are a shining, vibrant purple! Her shoulders aren't hunched over...she's just a normal, happy human being...with infectiously positive friends."
    
    scene bg sadie livingroom day with fade

    "The second my backside hits the sofa Haley wraps herself around me and starts talking."
    "We talk for a few minutes about my session, but given that she was a huge part of the subject matter I try to keep this as brief as possible. Luckily for me, she doesn't do her usual and push me for more information, she has plenty of other things to talk about...unluckily for me, it's mostly about Dominic and how he's coming over later once the match finishes..."
    "I say a silent goodbye to my favorite t-shirt."
    "She talks more about Dominic's impending visit and I resist the urge to ask her why she hasn't ended things yet. I imagine she felt about Erin the way I feel about Dominic. She was patient with me while I made my decision, the least I can do is return the favor."
    "Eventually conversation moves on to work and a climbing trip she's planning with some friends over the summer, then the man himself arrives..."    
    #Douche arives woho
    dominic "Evening ladies!" 
    "Dominic shouts, or perhaps slurs would be more accurate as he crashes into the room."
    "Haley sits up and scowls at him, her arms remaining wrapped around me."
    h_haley "I take it they won then?" 
    "She asks shortly, taking in his drunken state."
    dominic "Course they did babe, never in doubt." 
    "He staggers over to us and pulls Haley roughly to her feet, leaving me feeling as though I've just stepped out of a warm shower and into a freezing cold room"
    #yikes people will dislike this..
    dominic "You're in for a treat tonight princess."
    h_haley "I'm actually not done talking to Holly yet!" 
    "She says firmly, pulling her arms from his grasp."
    dominic "Oh but you are babes, I've got a big problem I could use your help with."
    "I try not to retch as he reaches around her waist and grabs her ass, giving me a wink as he does so" 
    dominic "Thanks for keeping her warm Holly, saves me a job."
    #dominic discusting wink ;)
    "He laughs shortly and gives me another wink I don't appreciate."
    holly "I'll see you in the morning then Haley?" 
    "I say, raising my eyebrows as a way of questioning that she's OK."
    h_haley "In the morning." 
    "She nods and gives me a quick smile."
    "I don't believe her, I actually feel my chest tighten a little anxiously at her smile, it looked forced and it feels to me like the last thing she wants is a night with Dominic! But what can I do? She said she's OK and she left willingly...and I suppose he is her boyfriend, she must be at least a little bit attracted to him."
    #easeout haley dominic
    "A shudder passes through my body as Dominic drags a beet red Haley off towards her room for what I gather he thinks will be a night of passionate, hot sex."
    h_haley "Have a good evening Holly." 
    #haleyblush
    "Haley blushes as she's escorted firmly from the room."
    "The door closes behind them and I sigh loudly. The thought of Dominic's hands all over Haley makes my skin crawl and I wonder, yet again, what the hell she sees in him and why she would ever want to get back together with him. She could do so much better..."
    "Ah well, I think, it's her choice, if she wants to be with him then she wants to be with him. There's nothing I can do about it."
    
    scene h_bg star with dissolve 
    #show holly beth haley 
    "After a long, disrupted night of listening to Haley and Dominic having sex I finally give up on trying to sleep and roll over to find my alarm reads 6:13am, sighing loudly I drag my tired body from my bed and head for the kitchen."
    "I make myself a cup of tea and sit down at the table, resting my head in my hands."
    h_bethany "Morning Holly," 
    "Beth laughs, entering the kitchen to grab her things for work" 
    h_bethany "did you not sleep either?"
    "I shake my head and look up to see Haley walking through the door...wearing my now old favorite shirt."
    h_bethany "Well good morning Haley!" 
    "Beth announces, as though welcoming a special guest" 
    h_bethany "It sounds like someone had a great night last night!"
    h_haley "Someone did yeah," 
    "she replies darkly" 
    h_haley "But it certainly wasn't me!"
    h_bethany "Wow," 
    "Nat continues, giving her an impressed look"
    h_bethany "you must be a freak between the sheets for Dominic to make that much noise all night."
    h_haley "I wouldn't go that far," 
    "She replies without smiling"
    h_haley "I woke up at 3 to find him humping my leg."
    h_bethany "Nice..." 
    #bethany frown
    h_haley "Isn't it just." 
    "Haley states, grabbing a glass of water and turning on her heel to head back to bed"
    h_haley "Sorry if he kept you up all night guys."
    #haley easeout with fade
    holly "She could do so much better." 
    "I say to Beth when I hear her bedroom door close."
    h_bethany "She could." 
    holly "How did Dominic even get her attention in the first place?"
    h_bethany "I don't know, why...are you interested?"
    holly "No!" 
    "I answer quickly" 
    holly "I just don't understand what she sees in him, what do you think it is?"
    h_bethany "I really don't know, I agree completely, she could do way better. Maybe you should ask her out and show her what dating  should be like..." 
    #bethany smirk
    h_bethany "She's already wearing your favorite clothes...you're practically halfway to married."
    holly "As we've discussed many times before, she's straight Beth." I scowl "I don't have the right equipment to make her happy."
    h_bethany "Hmmm, maybe," 
    #bethany smile 
    h_bethany "only one way to know for sure though..."
    "She gives me that look again as she finishes packing her lunch."
    h_bethany "It's not that hard Holly," 
    #bethany flabergast
    h_bethany "Keep thinking about it and you'll see where I'm coming from. Have a good one!"
    holly "And that's now my ex-favorite shirt by the way!" 
    "I shout after her as she heads for the door" 
    holly "I won't be able to look at it anymore without thinking about Dominic!"

    title "April"
    scene bg sadie livingroom day blur 

    nvl clear
    nvl_narrator "Paul and I were finally friends again. I walked in after my first day back at work to find him sat in my room waiting for me. He apologized for forcing Erin on me instead of listening to what I wanted and for saying he thought I was sick, and I apologized for blaming him completely for the whole situation I'd found myself in over the past few months."
    nvl_narrator "We talked for ages that night, more than we had done in months. The longer we talked the more I appreciated what Haley had tried to tell me, he had just panicked. He thought that I'd suddenly just 'get better', that I'd wake up one day and be the way I used to be. That second slide back into darkness had thrown him a lot more than I knew."
    nvl_narrator "We both cried in the end, Paul because he was so sorry for what had happened, and me because I was so relieved that he finally understood just how difficult it was dealing with what I was going through."
    nvl_narrator "Things between Haley and Dominic however, were exactly the same as they had been. It had been two months since she had first mentioned to me that she was thinking of ending things with him...but despite this they were still together and still having loud, apparently unsatisfactory sex at least three times a week...she was also still walking around in my ex-favorite t-shirt, flaunting it at every opportunity as if she was trying to see how far she could push it before I said something."
    
    scene bg connie bedroom clean dark
    #show holly haley 

    "I was laid in bed one night around the middle of the month watching tv and thinking longingly of the weekend, it had been a hell of a long week at work but I was finally starting to feel more settled again after the problems I'd faced earlier in the year. I heard the front door open and sighed deeply, Haley and Dominic were back from date night..."
    "Expecting to hear the sound of Haley's bedroom door closing, I was surprised when mine opened instead."
    h_haley "Holly!" 
    "Haley whispers loudly" 
    h_haley "Are you awake?"
    holly "Yeah." 
    "I prop myself up on my elbows and look over at her."
    #with move right -> left
    "She staggers over, clearly drunk, and clumsily removes her shoes before laying down beside me on the bed."
    holly "Are you OK?" 
    "I ask, pushing her hair back and revealing the mascara smudged down her cheeks."
    h_haley "I'm fine..." 
    "she slurs massively"
    h_haley "I've just had a few drinks is all..."
    holly "Just a few?" 
    "I raise an eyebrow" 
    holly "Where's Dominic?"
    #sad haley 
    h_haley "He fucked off wi- with his mates," 
    "she hiccups and turns onto her side" 
    h_haley "So I had a few drinks by myself and then Geoff put me in a taxi and I came ho- home."
    holly "Who the hell is Geoff?!" 
    "I demand, absolutely fuming that a stranger had had to put her in a taxi home and take care of her while Dominic was out having fun."
    h_haley "Geoff is a very kind man who works at a pub...bar...alcohol place in town...and who made sure I got in a taxi home..."
    #holly concerned
    holly "Why didn't you phone me? I would've come to fetch you."
    h_haley "I thought Dominic would bring me home...until he didn't come back..."
    holly "Oh Haley..." 
    "I slide out of bed and grab the wipes from my dressing table" 
    holly "why do you put up with this idiot, he can't even work out that he's meant to spend date night with you! You know, since you're his girlfriend and all..."
    "This comes out a little more scathingly than I intended and Haley's eyes begin to well up."
    holly "I'm sorry sweetheart" 
    "I sigh and start tenderly wiping the make-up from her reddening cheeks" 
    holly "I know he's your boyfriend it just...well it just winds me up that he's got a smoking hot woman like you and instead he ditches you to get pissed with his mates."
    h_haley "Thanks Holly." 
    "She clumsily cups my cheek in her hand and leans in, giving me a quick peck on the lips."
    "I freeze at this and Haley pulls back slightly."
    "With her eyes glued to my lips she leans in again and presses her mouth to mine. I don't move. My body feels as though it's been separated from my mind."
    "She pulls away once more and looks up at me, visibly embarrassed."
    h_haley "Sorry..." 
    "She blushes as I bring my fingers to my lips" 
    h_haley "I'm gonna go get some teeth and brush my water OK...I'll be right back..." 
    "She falls over her shoes and staggers back out of the room with only half her face make-up free."
    #easeout haley stagger??
    "Leaving the door wide open she heads for the bathroom and I hear the sound of a glass hitting the side of the sink, luckily it doesn't sound as though it's smashed. After a few seconds pause she starts to brush her teeth and then heads for her room."
    "I strain my ears, listening out for any sound that might indicate she needs my help, but she reappears in my doorway only moments later."
    #show haley again
    "The first thing I notice is that she's managed to get changed into a pair of joggers...and that damned t-shirt again."
    holly "Feeling better?"
    #holly smile 
    "I ask with a smile. Half of her face is still covered in mascara and she's now got toothpaste down her chin...it's an oddly endearing sight."
    "She nods and staggers back across to my bed once more. Pulling back the duvet she invites herself in and lays down, her eyes closing the second her head hits the pillow. I chuckle to myself and take another wipe from the packet. Tilting her face upwards slightly I finish tidying her up and get up to close the door."
    h_haley "Where are you going?" 
    "She cries drunkenly when she feels my weight leave the bed."
    holly "Shhhh," 
    "I whisper, brushing some hair back from her face"
    holly "I'm only closing the door."
    "I push the door closed and slide back into bed beside her. We only shared for a few nights back in January, the guilt I felt meant that I was soon back in my room, but I can't deny that I've missed this. No sooner have I settled back into bed than Haley wraps her arms around me and snuggles in closer."
    #haley tears but angry? dafuq
    h_haley "He's such a dick!" 
    "She exclaims suddenly and bursts into drunken, angry tears."
    holly "He definitely is." 
    "I whisper in agreement, drawing patterns across her back with my fingertips."
    h_haley "And he hates this shirt too," 
    "she adds as an afterthought" 
    h_haley "Which makes him even more of a dick!"
    holly "I don't think hating a shirt makes him a dick Haley, not everyone likes-"
    h_haley "He doesn't not like it because of what it is...he hates it because it's yours..."
    holly "And he thinks you should be wearing his clothes?" 
    "She shakes her head" 
    h_haley "He asked me why I liked wearing it so much and I just blurted out that it was because it smelt like you and I found it comforting...he was so pissed he just got up and left."
    holly "Oh." 
    #holly suprised
    h_haley "Yeah...but he isn't bothered if I wear his clothes, he thinks I should wear nothing whenever he's around," 
    "She sniffs" 
    "Easier access and all that. All he wants me for is sex...he doesn't even know when my birthday is and we've been together three fucking years!"
    "Her tears strengthen again and I grip her waist tighter with one hand while I run my fingers through her hair."
    holly "Sshhhh," 
    "I kiss the top of her head" 
    holly "try and go to sleep sweetheart. We'll talk about it more tomorrow."
    "I roll over so I'm flat on my back and Haley rests her head on my stomach, just below my breasts. Her fingers grip my shirt and I resume drawing patterns on her back in an attempt to calm her enough that she can drift off to sleep. I'm so pissed off with Dominic that I could use some time to sleep it off too, I'm almost certain that Haley wants to end things with him but I can't let her do it based on my feelings on the situation."

    scene black with fade
    scene bg connie bedroom clean day

    "The sound of my alarm going off wakes me early the next morning. I reach over to switch it off and look across at Haley, she had rolled over in the middle of the night and was still snoring gently beside me. Her t-shirt had ridden up slightly during the night revealing her perfectly flat stomach and creamy white skin. It took a serious amount of willpower to resist reaching out and touching it."
    holly "Haley." 
    "I whisper, gently shaking her shoulder" 
    holly "Haley, wake up sweetheart, it's time for work."
    h_haley "Hmmm...noooo..." 
    "She moans" 
    h_haley "not today."
    holly "Haley come on, it's Friday, just eight hours to go and it's the weekend."
    h_haley "Nooo..." 
    "She moans again, pulling the duvet firmly over her head."

    "I didn't spend too much time trying to convince her to get up, I knew I was fighting a losing battle and to be honest, I didn't blame her for wanting to stay in bed. Before I left I set her another alarm in case she was feeling up to going in to work later, placed some paracetamol and a glass of water on the bedside table for her and cleared a path to the door so there was less risk of her falling over her shoes again."

    scene h_bg day with dissolve 
    
    "My day at work passed slowly, I texted Haley at lunchtime but received no response. Bethany and Paul hadn't heard from her either."
    "The mountain of paperwork I was working through felt never ending as I willed the clock to tick round to clocking off time."

    scene h_bg dusk with dissolve 

    I finally walked through the door after a long day and a horrific journey home expecting to find Haley downstairs. I looked everywhere for her before heading upstairs to get changed, I poked my head around her bedroom door to find her bed still perfectly made and the room deserted.

    scene connie bedroom clean day 
    
    "Assuming she was either at work or climbing I pushed open the door to my room and started unbuttoning my shirt, ready for comfy clothes and some food...I nearly had a heart attack when my duvet started moving and Haley's mess of blonde hair came into view."
    holly "Have you been there all day?" 
    "I ask incredulously."
    "She nods and holds her arms out to me, her eyes round and pleading...how the hell does Dominic not find her irresistible?!"
    h_haley "Please Holly..."
    "I slip out of my shirt and replace it with a hoodie before walking across to her and pulling her in close."
    h_haley "I- I'm so sorry about last night," 
    "she mumbles against my chest" 
    h_haley "I shouldn't have kissed you, it wasn't right, I was drunk an-"
    holly "Haley it's fine, honestly, let's just forget about it OK?"
    "She takes one slow deep breath but otherwise doesn't make a sound as I wrap her more tightly in my arms and hold her tight."
    holly"You fancy something to eat?" 
    "I ask as my stomach starts to grumble some fifteen minutes later."
    "She nods her head and loosens her grip enough that I can move away from her."
    h_haley "I think I've got some leftovers in the fridge that we can just warm up."
    "I step backwards and breathe a sigh of relief as I finally manage to get my tight work trousers undone. Her eyes follow me across the room as I pull out a pair of shorts and quickly make the swap."
    holly "Coming?" 
    "I inquire, standing in the doorway and holding out a hand to her." 
    h_bethany "Think about it, she steals your favorite shirt...the one that you went mental about when I thought I might have accidentally shrunk it in the wash...and wears it almost constantly, even when she's with Dominic...which I know pisses you off so much you could punch something...yet you just let it slide and say nothing because she's Haley and you'd do anything for her."
    h_bethany "She came home last night absolutely devastated about Dominic and your bed was the only place she wanted to be. I was home too last night, Paul's away, she could've come and got in bed with me...because let's be honest, I give amazing cuddles...but no, she wanted you...and I bet she just held her arms out and you went running-" 
    "I feel my cheeks flush" 
    #holly blush
    h_bethany "because you just can't help yourself...and she'll have been there with the puppy dog eyes, desperate for you to hold her, because she lo-"
    #show haley easein
    "She stops abruptly as we hear a bang and a gasp of pain come from the hallway, she opens the door as the microwave pings to find Haley stood rubbing her knee."
    h_haley "That bloody table! I walk into it every time...I think I might still be a little bit drunk too you know..."
    h_bethany "Please tell me you're going to end whatever this is with him." 
    "Bethany says sympathetically as she pulls Haley into the room and sits her down at the table"
    h_bethany "He's about as decent a human being as bloody Erin!" 
    "She glances over at me and I frown at her."
    h_haley "Maybe we should introduce them to each other." 
    "Haley mumbles through a mouthful of food."
    h_bethany "They'd be well suited..." 
    "Bethany agrees, taking her dinner from the microwave and sitting beside her"
    h_bethany "Although not as well suited as the people they were with..."
    "Haley coughs and chokes on her food while I turn bright red and turn my attention back to the microwave."
    h_bethany "So," 
    "Bethany continues, completely unabashed"
    h_bethany "What is the plan with Dominic?"
    h_haley "I don't know,"
    #haley sad 
    "Haley shrugs, her eyes still streaming"
    h_haley "I know I should end it...but I kind of want to do it in some big, dramatic, public fashion where he looks like the complete tosser he is." 
    "She pauses and I take the seat across from her" 
    h_haley "Then once I've done that maybe I'll get with Holly..."
    #holly blush 
    "She winks at me and grins, while I look down and blush again."

    title "Revelations"

    scene connie kitchen day
    #show holly 

    "The night before my final exam."
    "I was sitting in the kitchen with my notes spread across the table, my head in my hands, fingers rubbing circles on my temple in an attempt to stop the incoming headache, when a quiet voice filtered in from the doorway."
    temp_char "Wow...this looks like fun..."
    #show haley with dissolve?
    "I look up as Haley comes in from her run, her face slightly red, a small bead of sweat running down her chest between her breasts. She sweeps her hair back from her face,"
    h_haley "Want some help?" 
    #very smiley haley
    holly "Depends, how much do you know about psychology? #cheeky" 
    h_haley "Not a lot," 
    "She laughs, moving to stand behind me" 
    h_haley "But I can take over that head massage for you if you like?"
    "Her fingers come to rest lightly on the top of my head and she moves my hands gently out of the way."
    h_haley "Close your eyes and relax Holly." 
    "She pulls my chair away from the table and runs her nails lightly over my scalp, sending shivers down my spine" 
    h_haley "Trust me, I know what I'm doing." 
    holly "That's nice." 
    "I breathe, dropping my pen on the table and sighing deeply as I lean back in my chair."
    "She presses more firmly and I feel my concentration start to wane, she wasn't lying when she said she knew what she was doing. Her thumbs press against the top of my neck and push gently outwards causing me to sink down into my chair."
    "Slowly her attention shifts from my scalp down the back of my neck and across my shoulders and I lose myself completely."
    with fade
    #transition
    "What must be hours later I feel her move round to my left and her fingers gradually leave my body."
    h_haley "Better?" 
    "She whispers against my ear."
    holly "Mmmm." 
    #holly closed eyes
    "Her fingers run down my arm before she suddenly straddles my lap and wraps her arms around my neck."
    holly "Jesus!" 
    "I laugh in surprise, opening my eyes to find her grinning at me" 
    h_haley "Is this how you plan on getting rid of me, getting me nice and relaxed then scaring me to death?"
    h_haley "I could think of worse ways to go." 
    "She leans in closer"
    h_haley "Do I smell bad?"
    "I tilt my head to her neck and sniff" 
    holly "Not really."
    h_haley "Good." 
    "She whispers, nudging her nose against mine and leaning fully into my body" 
    h_haley "You'd better ace this exam now I've put all this effort in."
    holly "I'll try my best." 
    "I yawn and glance at the clock" 
    holly "I should get ready for bed really; it starts at half nine. I don't wanna be sat there falling asl-"
    "The front door slams open."
    #sound door.mov dominic easein
    dominic "Haley!" 
    "Dominic's voice booms down the hallway."
    h_haley "Shit!" 
    #haleyeaseout
    "She jumps up off my lap and heads to meet him."
    dominic "What the fuck does this mean?!" 
    "He shouts angrily."
    h_haley "It means exactly what it says it means!" 
    "Haley shouts back"
    h_haley "I'm not arguing with you about this here, you want to talk about it, we'll go somewhere else and talk about it. I'm not having you dragging this shit out in my house!"
    dominic "Fine!!! I'll be outside. This is not over!!"
    h_haley "Argh!!" 
    "She screams into the empty hall before storming back into the kitchen"
    #easeinhaley 
    h_haley"As you probably just heard, I'm off out for a while." 
    h_haley "Don't wait up, don't worry, go to bed and get some sleep, smash your exam and I'll see you tomorrow when I get home from work. OK?"
    holly "Ok." 
    "I nod bewilderedly."
    #easeout 
    h_haley "Promise?"
    "She screams into the empty hall before storming back into the kitchen"
    #easein
    holly "Promise."
    h_haley "Ok great, I'll see you tomorrow." 
    "She smiles and pecks my cheek" 
    h_haley "Bye baby."
    "Baby? Where the hell did that come from?"

    scene bg connie bedroom clean dark with fade

    "I broke my promise that night."
    nvl_clear 
    nvl_narrator "I just couldn't fall asleep knowing that Haley was out with Dominic after their slanging match earlier, the fact that they'd gone in separate cars was all that kept me from getting myself overly worked up."
    nvl_narrator "It was just after midnight when she finally came home, I wanted desperately to climb into bed next to her, but I knew she'd be furious I was still awake. Instead I contented myself with knowing she was home and safe and managed to drift off."
    
    scene h_bg day 

    nvl_narrator "Overall my exam the following morning went well, I was desperate to make sure Haley was OK but managed to force myself to concentrate for the duration of the exam. I drove home as calmly as I could and spent the rest of the day lounging in the sun, drinking beer and reading my new book."

    scene bg sadie livingroom day
    #show bethany holly easein

    h_bethany "Hey Holly!" 
    "Bethany shouts, running across the room and jumping on me" 
    h_bethany "How was your exam? You look like you're enjoying being finished!"
    holly "It went well thanks...and yes, I'm loving being finished...I'm half way to hammered already." 
    "I grin and indicate my beer."
    #easeinpaul
    paul "Well then we'd better join you!" 
    "Paul yells, a box of beers materializing from nowhere."
    paul "Cheers!"
    #easeinhaley 
    h_haley "Hi guys!" 
    "Haley wanders over and pulls another beer out of the box."
    h_bethany "When did you get back?" 
    "Bethany asks, surprised"
    h_bethany "We didn't see you."
    h_haley "I pulled up literally as the front door closed." 
    "She laughs, laying down in the sofa next to me."
    h_haley "But you two were too busy touching each other up to notice me."
    paul "Ah well, we're all home together now...and there's beer...so all's well that ends well."
    holly "Definitely." 
    #holly grin?
    "I grin and raise my bottle."
    
    with fade
    #transition
    
    "A few blurry hours later Haley and I were sat chatting in the front room watching something random on tv. Bethany and Paul had gone to bed, both nursing sunburn and sore heads."
    holly "So, what happened with Dominic yesterday?" 
    "I ask as casually as I can manage."
    h_haley "He asked me to move back in with him."
    holly "Oh..." 
    "My heart drops."
    h_haley "Yeah...but I turned him down."
    holly "You did?"
    h_haley "I did," 
    #haleygrin
    h_haley "it's funny really, as soon as I said I wanted to end things he turned into this really sympathetic, nice guy. Like his personality just switched instantly. But I don't love him, hell, most of the time I don't even like him that much. I only got back with him to try and prove to myself that I wasn't in love with someone else."
    "Oh crap! I'd forgotten all about Haley's feelings for Paul!"
    holly "Did it work?" 
    "I ask quietly, hoping that her answer doesn't spell drama for Paul and Bethany."
    h_haley "Not even a little bit." 
    #sad haley 
    holly "I don't really know what to say to that."
    h_haley "Why, do you think this person doesn't love me back?" 
    "She asks, raising an eyebrow at me."
    holly "Well..." 
    "I pause, trying to think of the least harsh way of putting things" 
    holly "I think maybe they could do, in future, if their current relationship breaks down, but they're happy now so maybe you might want to think about it before you make any mov-"
    h_haley "What current relationship?" 
    "She interrupts quickly, an unbearably heartbroken look appearing on her face" 
    h_haley "They aren't in one as far as I'm aware!"
    holly "What? Ok, now I'm really confused. Who are you talking about?"
    h_haley "Jesus Holly!" 
    "She shouts exasperatedly"
    #add many expressions for god sake
    h_haley "I'm in love with you damn it!"
    "I stop talking in surprise and a deafening silence fills the space between us."
    holly "You...you love me?" 
    "I ask quietly."
    "Her eyes meet mine and she nods slowly."
    holly "But I...I..." 
    "I can't even finish that sentence, those seven words repeat over and over in my mind. She can't be in love with me..."
    holly "I thought you loved Paul?"
    h_haley "What?!" 
    "She asks incredulously"
    h_haley "Why the hell would you think that?"
    holly "Well...erm...bec-"
    h_haley "I love you Holly." 
    h_haley "I actually thought maybe you loved me too?" 
    "She pauses hopefully but I'm still so stunned by her admission that words just won't come out. The pain caused by my silence fills her face and my heart seems to shrivel up under my ribs."
    h_haley "I can't believe you haven't noticed..." 
    "She continues, her voice starting to shake" 
    h_haley "Unless...unless you have and you just haven't said anything because you don't feel the same way?"
    "A lone tear drips down her cheek as we sit staring at each other, I run my fingers through my hair and look away from Haley to the window, was Bethany right, have I really missed this?"
    #EASEOUT VERY QUICKLY MBY ANIMATION??? VERY FAST ZOOM ZOOM 
    "Without warning she turns and practically runs from the room, grabbing her coat as she goes."
    holly "Haley...wait!" 
    "I run after her but only get as far as the front door as it slams in my face."
    holly "For fucks sake!" 
    "I curse into the empty hallway and throw myself onto a step at the bottom of the stairs, my head in my hands."
    "She can't be in love with me, she's straight for god's sake! And surely I would've noticed if I was in love with her?"

    title "Session"
    scene bg corporate lobby small 
    #show blaire + holly

    "One week later. My latest session with Blaire."
    h_kisaragi "So Holly," 
    "Blaire smiles, tuning to a new page in her notebook"
    h_kisaragi "How've you been?"
    holly "OK I guess." 
    "She looks up at me curiously and leans back in her chair"
    h_kisaragi "OK. Where would you like to start today?"
    holly "I don't know really," 
    "I sigh, my gaze dropping to the floor" 
    holly "Where would you like to start?"
    h_kisaragi "Why don't we start with what's bothering you?" 
    #smile
    holly "Haley told me she's in love with me." 
    h_kisaragi "Is that not a good thing?" 
    "She asks, her eyebrows raising in surprise."
    holly "Well yes...I mean, maybe...or not really...I don't know..."
    h_kisaragi "Do you feel the same way?" 
    holly "I don't know..." I sigh again "I fucked it up anyway when I didn't say anything, so I guess it's pointless to worry about it now."
    h_kisaragi "Holly, look at me." 
    "Begrudgingly I tear my gaze from the floor."
    h_kisaragi "I want you to take a few minutes and think about this, think about Haley and then tell me how you feel."
    "I close my eyes, take a deep breath and cast my mind back over the last twelve months to the day I met Haley..."

    scene black with fade
    nvl_clear
    nvl_narrator "We had always gotten on well, that much was definitely true...and I had always thought she was gorgeous, again, definitely true, but that didn't mean she loved me...or I loved her, in fact, if anything that had made me even more aware that she was straight, the last thing I needed at the moment was to fall in love with a straight girl, that was one cliché I was determined not to apply to myself."
    nvl_narrator "I take several more deep breaths and try to focus on past events, most of the last year had been a blur of depression, anxiety and misery. But then...there was that day she walked in to find me sat sobbing on the living room floor...I remember the look on her face when Paul took over from that hug, I thought she was jealous it was me in his arms and not her...apparently not. Then that same night she came home with all my favourite things from the Chinese but had never actually asked me what I liked...she just knew. I remember the cuddles on the sofa and sharing her bed while I was getting over the nightmares, how worried she was when I spent that day at the park in the rain and how she took care of me that night...the look of utter devastation on her face when she thought there was someone else...fucking hell! I'm actually blind!"
    nvl_narrator "This revelation still doesn't cover my feelings towards Haley though, do I love her? If I've been blind to how she feels about me then it's entirely possible I've just ignored my feelings towards her...thinking about it, I've actually ignored my feelings towards a lot of things over the past twelve months, it was much easier to bury them than it was to acknowledge them..."
    nvl_narrator "I loved seeing her smile, I loved cuddling up with her on the sofa, sharing a bed with her had been a real comfort over the past few months, both physically and emotionally...then there's the fact my heart races every time she walks into the room..."

    scene bg corporate lobby small

    "I open my eyes, run my fingers through my hair and lean back in my the sofa."
    holly "Why does everything have to be so bloody complicated?!" I whisper.
    h_kisaragi "I take it that means you've realized that perhaps you do love this girl then?" 
    "Blaire asks, the corners of her mouth twitching slightly."
    holly "You knew?" 
    "I ask somewhat angrily."
    h_kisaragi "Holly,"
    #smile
    h_kisaragi "you've been coming to see me for over a year now and a huge part of my job is watching my patients' body language. Whenever we talk about Haley your whole aura seems to change, and no matter how desperately you tried to hide these feelings your face gave you away every time. The only question now is what you're going to do about it?"

    title "How Long?"
    scene bg sadie livingroom day blur with fade
    
    "September."

    "It had been three months since Haley had told me she loved me and it felt as though our relationship had changed forever."
    "Outside my love life I'd got my degree results and had managed by some miracle to achieve First Class Honors! I was down to seeing Blaire once every three weeks and hadn't cried at all in the last two sessions, I even joined a women's football team and played a game most weekends."
    "But it just wasn't right without Haley. We still spoke on a daily basis but it was strained and unnatural, that one four letter word was causing a chasm between us and I hated it. I wanted her to be there in the crowd when I played football, I wished she'd been there at my graduation. I missed her cuddles and hearing her talk about her day at work, or her friends...I missed seeing her walking around in my t-shirt."
    "Outwardly I was fine, but inside I was crumbling. I wanted my friend back."

    scene bg corporate lobby small with fade 

    title "Session"
    #show holly + blaire
    h_kisaragi "-Holly, are you with me?" Blaire asks.
    holly "Er...maybe...can you repeat the question?"
    "She sighs and puts her notepad on the table beside her."
    h_kisaragi "How's Haley?"
    holly "I don't know to be honest." 
    h_kisaragi "And how's Holly? Give me the truth this time please."
    #holly cry
    holly "She misses Haley." 
    "I sniff as my eyes start to well up."
    h_kisaragi "Does she think it might be time to let herself be happy? To push through the fear and tell Haley that she loves her too?" 
    holly "Y- yes..." 
    "I sob."
    h_kisaragi "Here Holly," 
    "I look up at the familiar box of tissues being held out in front of me"
    h_kisaragi "Take one."
    holly "Thanks." 
    "I smile as best I can through the tears."
    h_kisaragi "Right, now I want you to go home and tell that girl you love her."
    holly "I lo- love her? Y- y- you want me to open with that?"
    h_kisaragi "Open with whatever you like, the weather, last night's TV, a joke...the most important thing is that you're honest. Look at what denying this feeling is doing to you, how stifling it is keeping it all inside." 
    "She gestures to my current state."
    holly "You're right," 
    "I nod, standing up" 
    holly "I can't cope like this anymore. Even if she rejects me and breaks my heart, at least I can get over that in time instead of just spending all my time not knowing."
    h_kisaragi "Exactly." 
    #smile
    h_kisaragi "If you don't try you'll never know."

    scene connie kitchen day with dissolve
    #easeinholly 

    "I walk in after training and head for the kitchen to put my water bottle in the sink to wash later. I'm about to head upstairs and jump in the shower when I spot Haley sitting alone next to the open back door. I had intended to speak to her as soon as I got home from seeing Blaire but she was out when I returned."
    "I bite my lip and hesitate slightly before walking over to her."
    holly "Hi there, is it OK if I join you?"
    h_haley "If you want." 
    "She replies without looking at me."
    "I sit down and lean against the opposite side of the door frame."
    holly "So, I went to see Blaire this morning."
    h_haley "How did that go?" 
    "She asks, turning to face me."
    holly "She er," 
    "I stammer" 
    "She was pretty blunt, well, more so than normal anyway...I guess you could say she's fed up of how clueless I've been for the past few months."
    h_haley "She's laughing at me as well then?!" 
    "Haley snaps in a harsh tone that doesn't quite cover the hurt and embarrassment in her voice."
    holly "No! Not at all," 
    holly "No one's laughing at you I promise. It's me that everyone's annoyed with. She's fed up of how clueless I've been about my feelings. Just like Beth...and Paul...and you. I'm so sorry Haley, I never meant to hurt you."
    h_haley "That's OK Holly," 
    "She sigh"
    h_haley "It's not your fault you don't feel the same way I do. Maybe one day I'll get over you."
    "I look up at her to see her eyes welling with tears."
    holly "I never actually said didn't feel the same way..." 
    "I mumble"
    holly "And I really, really, don't want you to get over me."
    "I run my fingers up her calf and she raises a puzzled eyebrow at me."
    holly "I miss you Haley, but I don't want things to go back to the way they were before...I want them to go forward...to a better place than they were before...if you know what I mean?"
    "I can see the slight beginnings of a smile starting to show on her face when she realizes what I'm doing a terrible job of trying to say."
    h_haley "Really?"
    holly "Really." 
    #holly grin
    "Her smile widens and she rests her hand on top of mine as she looks back out across the garden. Gathering my courage, I slowly turn my hand over and lace my fingers through hers. Her grip instantly tightens in a reassuring sort of way and I slide across to sit beside her."
    holly "I did notice some stuff you know." 
    holly "All those months ago..."
    h_haley "Hmmm?" 
    "She looks questioningly at me"
    h_haley "What did you notice?"
    holly "Well, unfortunately nothing that would've prevented what's happened."
    holly "But I noticed you were gorgeous; I couldn't believe I didn't remember you when we met last year! I noticed you were smart and funny and you made me forget about all the shit stuff that happened. I noticed how safe I felt in your arms at night and how much I missed you during the day...but then I remembered that we were friends...and you were straight...I refused to risk losing you by trying to start something."
    h_haley "I understand that Holly."
    #sadsmile?
    h_haley "To be honest, I'm still really confused about everything. I mean, I know I love you, but it's like, does this make me a lesbian now? I've never had these feelings for a woman before. It took me ages to accept what that little voice in my head kept telling me, that I loved you more than I'd love someone who was just a close friend and the thought of losing you stopped me from trying anything too. But what I do know," 
    "She grips my hand tighter" 
    h_haley "Is that I would never just walk away from you...I'm way too attached."
    "Looking into her eyes I see nothing but honesty in her expression."
    "She licks her lips nervously and takes a shaky breath before leaning in closer. Following her lead, I meet her half way and she presses her lips to mine."
    holly "We don't need to add any labels to anything." 
    "I whisper" 
    holly "To you, to me, to whatever this might or might not turn into. But I need you to promise me one thing..."
    h_haley "Anything." 
    "She whispers, looking up at me with puppy dog eyes."
    holly "I need you to promise that you'll tell me if you decide you don't want this...as soon as you decide you don't want it...I've done break-ups before and they're awful. But you mean so much to me I don't think I co-"
    h_haley "Holly, stop." 
    "She puts a finger to my lips and shakes her head"
    h_haley "I feel the same way, the thought of losing you is almost unbearable...but at the same time, I'd be gutted if we didn't try this...I want to be with you...if you want to be with me?" 
    "I pause, my heart racing beneath my ribs. I want to just say yes, to just let myself fall so deeply in love with her that the thought of not being with her is laughable, to kiss her and hug her for no reason other than I feel like it...to take her to bed and show her what great sex feels like..."
    "But I'm scared, I'm terrified that things will change or I'll fuck everything up and lose her...and even though I trust her, I'm terrified of letting her in and her ripping my heart out..."  
    holly "I-" 
    h_haley "It's OK Holly." 
    "She smiles and kisses my cheek" 
    h_haley "I can practically hear the thoughts whizzing round in your head."
    holly "It's not that I don't want to,I'm just sc-"
    h_haley "Scared... But...since I'm scared too...shall we just take it slow, see how it goes and be scared together?"
    holly "I- yeah...I'd like that." 
    h_haley "Good." 
    "She kisses my cheek again and cuddles into my side, wrapping her arms around mine for good measure."

    "We sat like that for at least an hour, our bodies gradually pressed closer together as we simultaneously shivered while watching the rain pour down on the garden. The clock had ticked round to eight-thirty before we parted and Haley headed off to her climbing session"

    scene connie kitchen day with fade
    #show holly and beth easeinright 

    "I was still struggling to finish my tea when Bethany walked back in from work."
    h_bethany "Hey Holly. How's today been, did you go to your session with Blaire?"
    holly "Hey Beth, it's been OK thanks...and yes I went to my session."
    h_bethany "What's with that voice? Was it that bad."
    holly "No, it was fine...we talked about Haley again though."
    h_bethany "You did?!" 
    "Quick as a flash she pulls out the chair to my left and sits down next to me with an excited smirk on her face"
    h_bethany "Tell me everything! Have you finally come to your senses?"
    holly "Kind of yeah...well, maybe...not in so many word-"
    h_bethany "Jesus Holly! Don't ever take up storytelling will you! We'll never get to the good stuff!"
    holly "There isn't any 'good stuff'. At least not yet anyway. All that's happened is we've sat on the kitchen floor, held hands, talked a bit and sort of kissed...then Haley went climbing and I made a start at eating this."
    h_bethany "But you're going to get to the good stuff soon, right?" She asks eagerly.
    holly "I don't know. I don't want to fuck it all up, I mean, last time I checked she liked men Bethany. And I'm not saying she doesn't feel things for me, but I'm definitely not a bloke. I don't want to freak her out by going too fast."
    h_bethany "Oh sweetie," 
    "Bethany coos, tucking some hair behind my ear"
    h_bethany "I love how worried you are about this, but trust me, that girl has wanted you for so long now that jumping her as soon as she walks back through that door wouldn't be too fast!"

    scene connie bedroom clean dark

    "I lay on my bed and think on Bethany's words for the rest of the evening, by the sounds of things she's spoken to Haley about this a lot...which means that maybe Haley was just nervous earlier and was expecting more kissing that conversation...perhaps I might actually be over thinking this."
    "A glance at the clock tells me that Haley will be home soon, maybe I should be there to greet her..."
    with fade
    #transition

    "The sound of a key turning in the lock brings my focus back to the present, I look up as the door opens and Haley walks through it."

    #scene hallway 

    "I stand from my spot on the bottom step as she enters the cramped hallway and she jumps, clearly not expecting me to be waiting for her."
    h_haley "Jesus Holly! You scared me half to death! What're you doing sitting in the dark?"
    holly "I- well, I was waiting for you...it's something Bethany said...sorry...I- I'll go back upstairs..." 
    "I stammer, turning back to the stairs, my face burning in embarrassment."
    h_haley "No, don't!" 
    "She shouts, pulling off her coat"
    h_haley "Come here."
    "She pulls me into the front room and sits down on the sofa, dragging me with her."
    h_haley "You don't have to be embarrassed to be waiting for me you know." 
    "She smiles, cupping my still burning cheek in her cool palm."
    holly "I was going for some sort of romantic gesture, but it's been that long since I've...you know...I just froze when you walked in."
    h_haley "Maybe you should try again."
    "A cheeky grin spreads across her lips and I notice her skin is wet from the rain still falling outside."

    "I reach out and cup her face between my hands, my thumbs sweeping the water from her cheeks as I lean in and kiss the soft, damp skin. I pull away from her slightly and see her eyes widen. Not giving her more time to think I gently press my lips to her other cheek, her hands ball into nervous fists and she lets out a shaky breath."
    "Tilting my face to Haley, I nuzzle my nose against hers and she sighs quietly, I reach down and take her hands in mine, surprisingly she resists at first but the closer my lips get to hers the more relaxed she becomes."
    "I gently touch my lips to hers and then allow them to hover only millimeters away, leaving Haley to make the next move. She licks her lips slowly and tentatively edges closer once more, her fingers lace into mine before our lips meet again. I squeeze her hands reassuringly and she leans clumsily into my body, the kiss deepens and I slide the tip of my tongue over her bottom lip. Her mouth opens just enough to allow me access and she moans quietly, I don't think I'll ever get over hearing that noise come out of her mouth, I wrap my arms around her waist and pull her body flush against me."
    holly "Is this OK?" 
    h_haley "More than OK." 
    "She smiles, the expression etched on her face melting my heart...I can't believe I've been so blind to this."
    "Haley's grin widens, her hands cup my cheeks and suddenly we're a mash of lips, teeth and tongues. She moans as I press against her and push her down into the sofa, my fingers fumble with the zip on her jacket as I try desperately to remove it from her body, her fingers come to my jumper and we share a quiet laugh as we simultaneously find ourselves tangled together. The pause is kept brief as we shed clothes and resume kissing fiercely, I slide my knee between her thighs and am just about to trail my lips down her neck when I feel her hands on my shoulders, pushing me away."
    holly "Shit! Sorry Haley," 
    "I stop instantly and sit up" 
    holly "I got carried away, I forgot this was all new to you...and we're meant to be taking things slow..."
    h_haley "It's not that..." 
    "She blushes"
    h_haley "Well OK, so maybe it is a little bit...but I was kind of thinking maybe...would y-" 
    "she clears her throat" 
    h_haley "Would you like to take this somewhere more comfortable?"
    holly "Only if that's what you want." 
    "I smile and kiss her again."
    "She laughs and her smile widens" 
    h_haley "I've dreamt of asking you that for months, it's definitely what I want."
    "She takes my hand and leads me upstairs to her room."
    #hide easeout etc
    scene bg leona room dark with fade

    h_haley "I can't explain how badly I've wanted this Holly."
    "Haley sights, her fingers trailing lightly from my knee up to my tigh"
    h_haley "I almost can't believe we're really here now."
    "She nuzzles into my neck *OwO* *What's this* and squeezes my tight, causing a small ripple of pleasure between my legs."
    holly "It feels pretty real to me." 
    "I smile and pull her in tighter." 
    "Her fingers find their way to the top of my thigh and she squeezes again. I try to stop the sensation this causes from showing on my face, but as she tilts her head up to kiss me once more Haley repeats the action and a quiet moan escapes my lips."
    h_haley "So I was thinking..." 
    "she grins as her fingers begin to stroke my leg" 
    h_haley "Maybe it'd feel more real if we had a bit less clothing contact and a bit more skin contact?"
    holly "Whatever you think is best." 
    "She sits up and pulls her shirt up over her head to reveal a firmly toned stomach and surprisingly large breasts encased in a sports bra, without pausing for effect she slips her joggers down over her bum and pulls them off."
    holly "W.. We.. Well," 
    "I stammer, my eyes firmly glued to her body" 
    holly "I guess that answers that."
    h_haley "It certainly does," 
    "She smirks and takes the hem of my top between her fingers" 
    h_haley "Although you're being incredibly slow following suit."
    "I sit up and let her take my top off, she throws it over her shoulder and quickly starts to undo my jeans. I allow her to remove them completely and then pull her down beside me once more."
    "My fingers traverse the almost visible muscles of her stomach and come to rest just below her bra. I hesitate before allowing myself any further movement, we haven't talked about it, but I assume I'm the first woman Haley had partially undressed in her bed, I don't want to rush this again or pressure her into anything."
    "My concerns however, are short-lived. Haley brings her hands to her bra and tugs playfully at the straps."
    h_haley "Would you like me to take this off for you?" 
    "She whispers against my ear."
    holly "What happened to taking it slow? Not that I'm complaining about this, but I thought you wanted to-"
    h_haley "I know...but sometimes willpower loses out to impulse, you know?"
    "She winks at me and kisses me once more" 
    h_haley "It's OK Holly, if you're OK, I'm OK too."
    "She smiles at me and rolls me onto my back, her lips meeting mine once more as she straddles my thighs. She takes my hands in hers and runs them up her body to just under the elastic of her bra"
    h_haley "You wanna help me out here sweetheart?" 
    "She winks suggestively and removes her hands."
    "I sit up as far as I can and kiss her again, my tongue meets hers as my thumbs slip under the elastic and I slowly begin to push upwards. She moans softly and kisses me with renewed passion when my thumbs brush over her already hard nipples."
    "Our lips part and I push the garment the final few inches over her head before looking down to admire her breasts."
    holly "Wow..." 
    "I breathe, leaning down to kiss each nipple" 
    holly "These are seriously impressive."
    h_haley "Really?" 
    holly "What do you mean, really?" 
    "I reply incredulously" 
    holly "You're gorgeous Haley...don't tell me you've gone shy all of a sudden..." 
    h_haley "No, I jus-"
    "I push myself against her, forcing her to lean further and further backwards until she's laid on her back, extracting my legs I crawl up her body and plant several kisses across her chest and up her neck."
    holly "You're beautiful Haley," 
    "I kiss just below her ear and she shivers" 
    holly "We don't have to do anything you don't want."
    h_haley "I appreciate the sentiment Holly," 
    "She gasps as my lips make further contact with her neck" 
    h_haley "but the last thing I want right now is for you to stop what you're doing!"
    "I nuzzle against her skin and bring my hands to her breasts, smiling happily as I test their weight and find them spilling over my palms. I'd never really considered myself a boob woman before, but I could easily spend hours paying this pair special attention."
    "Haley tangles the fingers of one hand in my hair while the other rests on my shoulder and applies a gentle pressure."
    holly "Trying to tell me something?" 
    "I whisper into her neck and pinch her nipples."
    h_haley "Ah!" 
    "She gasps" 
    h_haley "Please Holly...lower...I- I want you to suck them..."
    "A beet red blush spreads across her cheeks and chest as she makes this request, I can feel her body burning under mine as I kiss down her neck. I massage her breasts gently and press down on her nipples causing her grip in my hair to tighten."
    h_haley "Oh God Holly..." She breathes.
    "I push her breasts together and lick across both nipples before sucking them individually between my lips, Haley squirms underneath me and her breathing quickens. Quiet moans slip from her mouth as I continue to lavish attention on her breasts, the first nip causes her to jump and push her breast further into my waiting mouth. I can feel her heart racing under her ribs as I slide my fingers between her thighs."
    h_haley "Please Holly," 
    "She whimpers, her fingers leaving my hair and gripping my wrist" 
    h_haley "Please..."
    "I press my fingers against the damp material of her underwear and her breath catches in her throat, a long moan escapes her lips and I feel her thighs tighten around my hand. I rub the tips of two fingers in small circles over and around her clit."
    h_haley "Fuck! Holly!" 
    "Her fingers grasp my wrist tighter while the fingers of her other hand tangle in my hair once more" 
    h_haley "Oh God! Please don't stop, I'm gonna cum...please...please..."
    "I apply a touch more pressure to her clit and her thighs clamp hard around my hand, I can't believe how responsive she is, I've barely touched her."
    h_haley "Oh Jesus!" 
    "She whimpers, her body trembling, her face and chest flushed" 
    h_haley "I'm sorry Holly, I just couldn't stop myself...it's kind of been a while since I've...you know..."
    holly "With a partner?" 
    "I ask, planting several gentle kisses up her neck."
    h_haley "With anyone..." 
    #haleyblush
    holly "And here's me thinking I was just doing an incredible job." 
    "I laugh and kiss her lips."
    h_haley "You did an amazing job." 
    "She mumbles between kisses."
    holly "What do you mean did?" I ask.
    h_haley "She gasps as I hook the fingers of one hand into her pants, while the other rests on her ankle. Looking up at her face I remove the fingers from her pants and slide both hands slowly up her legs, my eyes never leaving hers."
    holly"Do you want me to stop?"
    "A strange expression appears on her lips and I catch her eyes welling up before she looks away."
    "I let go of her legs and lay down beside her, a horrible feeling setting in as I realize she's having second thoughts about this."
    holly "It's OK Haley," 
    "I kiss her cheek and try to swallow the emotion rising up through my chest" 
    holly "I said we wouldn't do anything you didn't want and I meant it."
    h_haley "I'm so sorry Holly," 
    "She wraps herself around me and I feel tears drip onto my skin" 
    h_haley "I want you, I really do, I'm just nervous and kind of freaking out an-...and I don't want you to think I've changed my mind or anything. I still love you, I-"
    holly "It's OK Haley." 
    "I repeat, swallowing hard once more"
    holly "There's no rush...go to sleep, we'll talk in the morning."
    "After a long and restless night for both of us we finally give up on sleep at around half seven. Haley rolls over to face me and gives me a small smile."
    h_haley "You're still here." 
    "She moves closer and presses her naked body against mine, I had put my shirt back on in the early hours of the morning" 
    h_haley "I was worried you'd leave."
    holly "I thought about it," 
    holly "I wasn't sure how you'd feel about me still being here this morning."
    h_haley "I want you here sweetheart." 
    "She kisses me softly" 
    h_haley "Last night I just...well I just panicked. I want you so much but you were right, we were meant to be taking things slow, I don't want to rush it and it not mean anything...not that last night meant nothing!" She adds hastily "I loved it! I jus- I just wanted it to be special...I've never felt how I feel about you with anyone before."
    "She blushes crimson."
    holly "I'll wait." "I whisper."
    h_haley "Really? That's OK?" 
    "She glances hopefully at me."
    holly "Really." 
    "I smile, the sinking feeling lifting as her words start to sink in"
    holly "Although you are very, very tempting."
    h_haley "Oh..." 
    "She looks down then turns over and starts looking for her t-shirt."
    holly "Don't," 
    #holly smile
    holly "I like you like this."
    h_haley "Flattery will get you everywhere." 
    "She turns back to me and kisses me again"
    h_haley "But even so, I should get dressed. I don't want to cause you too much turmoil laying here with so much skin on show and then not letting you touch it."
    holly "Can't I even look at it?" 
    h_haley "Hmmm," 
    "She pulls her shirt back over her head" 
    h_haley "nope."
    holly "Fine then." 
    "I giggle, rolling out of bed and pulling my jeans back on."
    h_haley "Hey!" 
    "She pouts, following me across the bed and hooking her fingers in my belt loops"
    h_haley "I said you couldn't touch, I didn't say you should get out of bed."
    holly "I don't want to risk temptation." 
    "I wink and stick my tongue out at her."
    h_haley "Well, I'm going back to bed." 
    "She kisses me again" 
    h_haley "You know where I am if you change your mind."
    holly "Noted." 
    "I grin as she falls back into bed and pulls the duvet over herself."
    "I leave the room and head downstairs to get a glass of water, shaking my head quickly to try and get thoughts of Haley half naked out of my head."
    "..."
    paul "Hey player!" 
    #enterkitchen
    "Paul yells as I enter the kitchen" 
    paul "I hear you and Haley finally accepted you're in love!"
    "I blush and dodge the question" 
    holly "Maybe...why are you up so early?"
    paul "Footy training this morning...and don't change the subject. Did you seal the deal or what?"
    holly "Kind of." 
    "I reply, as blasé as I can manage."
    "He looks puzzled" 
    paul "Kind of? What does that mean?"
    holly "It means that...well...we sort of got halfway through then Haley changed her mind."
    paul "Were you really that bad?" 
    #paulgrin
    holly "Maybe."
    holly "She said she wants to wait, that she wants it to be special."
    paul "To be fair that's not necessarily a bad thing pal, Beth wanted something similar and look where we are now."
    holly "I know. It's just, I really, really, really don't want this to be another failure. A random girl, maybe I could cope with that ending badly. But not Haley, she means way too much to me."
    paul "I know it's a bit more complicated for you lesbians, but trust what we've all been telling you. Haley really likes you! She wants to go full homo for you!"
    "He slaps me on the back as he heads out the door and I can't stop a huge smile from spreading across my face."
    #hollysmile 

    title "Good Things Come to Those Who Wait"

    nvl_clear
    nvl_narrator "I thought things would be awkward between Haley and I after she said she wanted to wait, but thankfully in reality, things were better than they'd been since long before I started seeing Blaire."

    nvl_narrator "We spent almost all our time together, doing nothing out of the ordinary or that could be deemed overly exciting, but to me it meant the world. She took me climbing and introduced me as her girlfriend the first time I met her friends. We went out for dinner, I let her share my dessert, she refused to let me pay and we walked home together holding hands, huddled together against the cold winter weather. Almost every night we would lay together on the sofa, just cuddling and talking about our days, or watching random TV."
    
    nvl_narrator "The only real time we were apart was when it came time for bed. We had shared before of course, but Haley was adamant that we sleep separately. I could understand why, our goodnight kisses were getting longer and more handsy with each day that passed, I wanted her naked in my bed and she knew it."

    nvl_narrator "The week before Christmas Bethany, Paul, Haley and I held our annual 'House mates Only' Christmas party, we all went our separate ways during Christmas week so it was nice to have an evening in with just the four of us."

    #sceneswitch chrismas?

    nvl_narrator "We exchanged gifts, played games and got drunk together. Bethany and Paul had a contest to see who could out-embarrass the other (Bethany won...4-minute sex episodes came into conversation again...) while Haley and I howled with laughter at some of their antics. They went to bed not long after this for Paul to prove he was better than Bethany had told us all he was, leaving me and Haley to take over the sofa and engage in a heavy, drunken make-out session which left us both breathless, hot and horny."

    nvl_narrator "I had had my knee firmly pressed between Haley's thighs, her jeans unbuttoned and her shirt almost off before she finally managed to tear herself away. My face must have been a picture as she sat up and refastened her jeans, a broad smile played on her lips before she kissed me once more and whispered in my ear:"

    h_haley "{i}Not yet baby.{/i}"

    "I flopped back down on the sofa as she went to bed, trying desperately hard to ignore the burning need throbbing between my legs."
    "After that last frustrating episode I made a point of keeping things brief where Haley was concerned, not because I didn't want her, in fact, I was starting to struggle just being in the same room, my mind was constantly in overdrive thinking about everything I wanted to do to her!"


    title "Christmas Eve."
    
    h_haley "Hey baby." 
    "I look up from my magazine to see Haley poking her head around the door to the front room."
    holly "Hey." 
    #hollyhappy
    h_haley "You all packed and ready to go?"
    holly "More or less." 
    "I throw the magazine on the table next me" 
    h_haley "You wanna do something this afternoon? I'm sure there's some Christmas TV we could watch."
    holly "Hmmm, maybe," 
    "She picks at the door frame with her nails" 
    holly "let's finish packing then I'm all yours."
    "I reach over to pick up the magazine again" 
    holly "Maybe in a bit, I hate packing."
    h_haley "Or maybe now." 
    "She raises an eyebrow at me and gives me a stern look."
    holly "Or-" 
    h_haley "Now, Holly!"
    holly "Alright, alright, Jesus, keep your hair on." 
    "I scramble up from the sofa and make my way to my room. I push the door open and find a neatly wrapped cardboard box on the edge of my bed, the tag simply reads, open me."
    "I perch on the edge of the bed and place the box on my lap, pulling open the ribbon I tear off the wrapping paper and lift the lid to reveal a strap on with two feminine lilac dildos attached, one for the wearer and one for their partner."
    h_haley "Do you like it?"
    holly "Jesus Christ!" 
    "I jump, clutching my chest and looking up to see Haley stood nervously in the doorway, biting her bottom lip."
    h_haley "I wasn't sure what sort of thing you'd like...or what would be best, so I went for that an-"
    holly "Haley it's great." 
    #hollysmile
    "Taking everything off my lap and standing up."
    h_haley "Wait! There's more." 
    "She rushes over to me and pushes me back down on the bed."
    "I look questioning up at her and she untie her dressing gown, I can feel myself starting to drool and she hasn't even shown any skin yet. Letting it drop from her shoulders she looks down at me and bites her bottom lip once more. I swallow hard, our eyes never leave each other's as the material slides down her body and pools at her feet."
    h_haley "Merry Christmas Holly." 
    "She smiles nervously and her head dips."
    "I follow her gaze and my breath catches in my throat, a thick red ribbon tied in a bow covers her breasts and she's wearing matching red lace French knickers."
    holly "Wow..." 
    "I breathe."
    h_haley "Do you like?" #haleyblush
    "I look back up at her and run my fingers over the curve of her hips, then up and across her back. Standing, I lean down and gently bite from her shoulder to her collar bone before kissing my way up her neck."
    holly "You look incredible." 
    "I whisper against her ear, nipping the lobe" 
    holly "But I thought you wanted to wait, are you sure you want this?"
    h_haley "More than sure." 
    "She gasps as I trace her ear with my tongue" 
    h_haley "The other day, when we were on the sofa, I wanted you so badly it took all my willpower to pull away...but after I stopped you the first ti- time...oh Jesus..."
    "Her head rolls back as I run my nails lightly down her back and start applying kisses to the other side of her neck."
    holly "You were saying..." 
    "I prompt, a smile playing on my lips."
    h_haley "After I stopped you," 
    "Her fingers grip my forearm" 
    h_haley "I knew I'd have to co- come up with something special to show you how much you mean to me...and how much I appreciate you waiting for me...mmmm..."
    "I squeeze her ass and sit down on the edge of my bed once more. Pulling her to me I scatter kisses over her chest and start to slowly untie the ribbon covering her breasts."
    h_haley "Oh God I want you Holly!" 
    "She cups my face in her hands and kisses me hard, her breathing hot and heavy."
    "I finish untying the ribbon just before Haley manages to climb onto the bed. She straddles my waist and proceeds to kiss me with raw passion, sliding her tongue into my mouth and grinding down in my lap. I can feel my underwear becoming slick and warm. I take her breasts in my hands and rub small circles on her nipples, delighting in pinching them every so often causing Haley to jerk against me."
    h_haley "Fuck Holly!" 
    "She moans and grinds down harder" 
    h_haley "Please...I need to..."
    holly "Wait sweetheart." 
    "I smile and hold her hands out to the side" 
    holly "You know I'll take care of you."
    "I push her gently from my lap, pull my t-shirt and joggers off, leaving me only wearing a thong, then lay down in the centre of my bed. Haley crawls seductively up the bed towards me, kissing from my ankles to the top of my thighs."
    h_haley "You look so pretty like this Holly." 
    "She kisses across the front of my underwear and grins up at me" 
    h_haley "I like the lack of a bra."
    holly "Thanks, my boobs are just small enough that I can get away with them not swinging round my knees without support."
    "She giggles and starts to pull my thong down my legs"
    h_haley "That's better." 
    "She drops the item on the floor behind her and lays down on top of me, placing her thigh firmly between my legs" 
    h_haley "Now, I've picked some bits and pieces up from you, but mostly I'm kinda flying blind here." 
    "A light pink blush tinges her cheeks" 
    h_haley "So just...just let me know...you know...how I'm doing an-"
    holly "Just do whatever feels natural to you." 
    "I smile and kiss her" 
    holly "You don't have to touch me if you don't want."
    h_haley "I do want." 
    "She smiles and places her hand between my breasts" 
    h_haley "I love that this is finally all mine to look at and touch...and taste." 
    "She takes my nipple between her lips and sucks gently."
    holly "That's good." "I gasp" 
    holly "Do more of that."
    "She grins up at me and swirls her tongue around my nipple before taking it back between her lips, her left hand runs down my body and she dips her fingers between my thighs. I can't help but tilt my hips upwards, encouraging her fingers to slide against me. She takes the initiative and tentatively presses closer, kissing her way up my neck."
    h_haley "I've always wondered what you taste like gorgeous." 
    "She whispers, slipping a finger inside me before bringing the glistening digit to her lips and licking it" 
    h_haley "It's almost as sweet as you." 
    "She winks, kissing me and pushing her tongue into my mouth."
    "I slide my hands down her back, lightly scratching with my nails. She moans into my mouth and begins to roll her hips, I match her rhythm and she pushes harder against my thigh. It becomes quickly apparent that she's found a spot she likes as she begins to gasp and pant. She slides her hand back between my thighs and rubs my clit."
    h_haley "Fuck!" 
    "I groan."
    h_haley "Do you like that?" 
    "She breathes."
    h_haley "God yes..." 
    "I bite her neck and she jerks against me."
    "I continue to nibble on her neck and slide my hands under the fabric of her underwear. Gripping her ass firmly I hold her against my thigh as she rocks harder and faster."
    h_haley "Oh God Holly!" 
    "She bursts out" 
    h_haley "I need to...fuck...I'm gonna...cum...Jesus..."
    holly "Me too... (classy fucking hentai everyone always cums together)" 
    "I gasp, the constant strumming of her fingers on my clit pushing me closer and closer to the orgasm that's eluded me for far too long."
    h_haley "I want us to cum together." 
    "She kisses me sweetly, clearing trying to hold back her orgasm."
    holly "I'm there Haley..." 
    "I squeeze her ass" 
    "Cum for me baby, just let go."
    h_haley "Holly..." 
    "She moans my name in such a way that it both drives me crazy and melts my heart at the same time, within seconds I feel my own orgasm crashing through my body. All those months of frustration with Erin and patient waiting with Haley forgotten instantly."
    holly "Don't stop!" 
    "I cry out as Haley's fingers leave my clit"
    holly "Please...please keep going..."
    "She smiles broadly and slides down my body, her pussy leaving a sticky, warm trail down my thigh despite the fact her underwear is still firmly on. The pause I was expecting doesn't come and as soon as she's able Haley reaches out her tongue and licks firmly across my slit."
    holly "Fuck...Haley...that's so fucking good!" 
    "I pant heavily. Her tongue laps at my opening and I look down at her to see she's smiling proudly, her brilliant PLACEHOLDER eyes dark and shining with excitement."
    "I take her hair and tangle my fingers in it, pulling gently. She follows the direction and moves her attention back to my clit, sliding two long, slender fingers inside me as she does so."
    holly "Ahhhh..." 
    "I moan as she hits that magic spot, already so close to a second orgasm that it takes even me by surprise" 
    holly "fi- fingers...up..." 
    "I manage to stammer."
    "Haley curls her fingers upwards and rapidly flicks her tongue over my clit, it's a little clumsy but she makes up for it with sheer enthusiasm and I'm soon cumming again. My fingers grip her hair tightly and my body shakes, the sheen of sweat covering me glistens in the light as my chest heaves. Haley dutifully remains between my legs, licking me clean and kissing softly over my still sensitive skin."
    "I sit up and take her face in my hands. Pulling her lips to mine I kiss her passionately and roll her onto her back."
    h_haley "Was that ok?" 
    "She asks between kisses."
    holly "That was waaayyyy more than OK sweetheart." 
    "I grin before she slips her tongue into my mouth" 
    holly "You taste of me." 
    "I observe."
    h_haley "Does that put you off?" 
    "She bites her bottom lip."
    holly "No," 
    "I laugh and shake my head" 
    holly "it's actually really hot...and speaking of hot..." 
    "I take her pants and pull them down over her bum, the material even more dark and wet than I'd imagined" 
    holly "I love the undies, don't get me wrong...but I've been dying to taste what's underneath."
    "She blushes beet red all over when I finally rid her of the last piece of clothing."
    holly "Something wrong?" 
    "I ask, concerned that I've upset her."
    h_haley "No," 
    "She kisses me" 
    h_haley "I was just thinking...much as I'm looking forward to seeing what you can do with your tongue...can we try out your present?"
    holly "My present?" 
    "I raise a mocking eyebrow."
    h_haley "Ok, ok, so it's more our present. But I'm itching to try it out...pretty please..."
    "I reach across her and grab the strap-on."
    h_haley "I cleaned it and everything," 
    "She says quickly" 
    h_haley "so we're good to go."
    "I smile and give her another kiss as I work the straps up my thighs."
    holly "You're so cute when your nervous." 
    "I brush her hair back from her face and she props herself up on her elbows to kiss me again."
    h_haley "I don't feel cute, I feel like I'm killing the mood."
    holly "You're not, I promise." 
    "I peck her lips and push the dildo into my pussy before adjusting the straps and tightening them to a secure and comfortable position."

    h_haley "I never thought I'd find the sight of a woman with a dick so attractive." She smiles and pulls me down on top of her.
    "She lays her legs over the back of my calves and slides her fingers into my hair as we engage in a make-out session to rival our time on the sofa after the Christmas party. I raise myself up enough that I can play with her breasts and lightly run my fingernails over her abs and across the curve of her hips and inner thighs."
    h_haley "You make me feel so good Holly..." 
    "She moans some minutes later as I along her jaw, her chest heaving" 
    h_haley "Please baby...inside..."
    "I slip my hand between her thighs and judge that she's definitely wet enough. The cock standing proudly between my legs isn't huge but it's by no means small either, rushing this would definitely kill the mood."
    "I press the head of the cock against her opening and watch as her swollen lips part willingly to accommodate it, she lifts her hips and moans loudly. Slowly I begin to rock my hips, edging the cock deeper and deeper with each gentle push until I'm in her to the hilt."
    holly "Ok baby?"
    h_haley "God yes." #Megasmile 
    h_haley "You gonna show me what you can do with this thing or what then?"
    "I laugh shortly and pull the toy almost all the way out of her before repeating my earlier action and sliding it agonizingly slow back in."
    h_haley "Hoooollllyyy!" 
    "She groans, crossing her ankles around my backside and lifting her hips in an attempt to speed up the process."
    holly "You said you wanted to see what I could do." 
    "I laugh" 
    holly "Let me show you."
    "I repeat this action again and again and watch as Haley gradually starts to relax, her legs slipping back down my thighs. Her eyes close and I lean down to kiss her, she opens her mouth instantly to allow my tongue to meet hers."
    h_haley "This is actually kind of nice," 
    "She murmurs without opening her eyes" 
    h_haley "it's almost therapeutic."
    "Convinced that she's now fully relaxed I increase the pace at which I slide the cock into her, pulling out and hitting that magic spot with each thrust of my hips. Small gasps and moans slip from her mouth and I make a point of pressing my clit to hers every so often."
    h_haley "Oh God." 
    "She breathes" 
    h_haley "Fuck, Holly this is amazing...you're incredible!"
    "I laugh into her neck and tilt my hips slightly upwards, once again increasing the pace."
    h_haley "Harder baby...please..." 
    "She locks her ankles tightly around my ass once again and this time I adhere to her request."
    "I raise myself up onto my knees and pull her down the bed a little. Her hands reach down and grip the waistband of the strap-on firmly."
    h_haley "Fuck me Holly...come on baby." 
    "She pants."
    "The muscles in her arms flex invitingly as she pulls me in deeper, the cock jackhammering into her dripping pussy. I slide my clit against hers with every stroke now, my own orgasm rapidly building at the sight her. She looks so sexy it's almost as though she can't possibly be real, her eyes firmly closed and her head thrown back as she bites her bottom lip, her abs clearly defined through her heavy breathing."
    h_haley "Oh fuck!" 
    "She moans suddenly, one of her hands reaching up to grab the headboard" 
    h_haley "Fuck...yes...baby...ohhhhh..."
    "Her hips jerk firmly under me and the grip of her ankles around my thighs loosens considerably. I don't stop and continue to slide the cock rapidly in and out of her before pushing it in deep and rubbing my clit firmly against hers."
    h_haley "Yes baby!" 
    "She kisses me hard and grabs my ass, pulling me to her" 
    h_haley "God...yes...fuck I- I'm...oh...oh..."
    "The rest of her words are drowned out by our combined moans and heavy breaths."
    "I collapse on top of her as my arms give out and she laughs" 
    h_haley "Now that...that was what I call sex!"
    holly "I'm glad you enjoyed it." 
    "I laugh with her."
    "I go to pull out of her but the hand still holding the waistband of the strap-on holds firm."
    h_haley "Don't!" 
    "She shouts feebly" 
    h_haley "Just...just give me a minute..." 
    "A smile appears on her lips" 
    h_haley "I thought I was good but Jesus Holly...I've never enjoyed sex more!"
    "Smiling, I lay down on top of her and take one of her nipples between my lips, using my tongue to play with it gently. Her hands come to my head and she runs her fingers softly through my hair."
    h_haley "I love you Holly." 
    holly "I love you too." 
    "I mumble through a mouthful of her breast."
    h_haley "Are you sure it's me you love?" 
    "She grins, looking down at me" 
    h_haley "Or do you prefer them?" 
    "She indicates her breasts."
    holly "Nah...don't get me wrong, these are nice..." 
    "I grin" 
    holly "but they could not exist at all and I'd still be just as crazy about you."
    "..."
    "Starting to get uncomfortable I pull away from her and slide the cock from her pussy before loosening the straps and removing its companion from between my thighs."
    h_haley "I'm glad we waited." 
    "Haley sighs as I lay back down beside her and cuddle into her side."
    holly "Hmmm..." 
    "I yawn" 
    holly "Me too sweetheart...me too."
    "She lifts her arm and I instantly move further into her embrace, I feel her lips press against the top of my head and drift off into a deep and contented sleep."

    with fade 
    #transition

    h_haley "Did you really not remember me?"
    holly "Hmmm?" 
    "I jerk awake and find Haley looking down at me. Lifting my head, I look over at the clock on my bedside table" 
    holly "Haley... It's five in the morning. Can this not wait a few hours?"
    h_haley "I awake now," 
    "She pouts"
    h_haley "Please baby, just answer the question."
    holly "OK, OK, fine. What's the question?"
    h_haley "When I moved in, did you really not remember me?"
    holly "Oh, erm, no...not really..." 
    "I mumble sheepishly" 
    holly "did you genuinely remember me?"
    #haleysmilebig 
    holly "How could I not?! I remember the first time we met, you came straight from work so you were still wearing your work clothes, that light blue blouse with those black fitted trousers..." 
    "She shuffles down and kisses me" 
    h_haley "You were absolutely stunning. I mean, Paul always said you were pretty, but he definitely didn't do you justice. I was completely mesmerized by you."
    "I feel myself blushing."
    h_haley "Then you spoke and I knew I was definitely in trouble." 
    "She runs her fingers through my hair" 
    h_haley "I loved your voice. And you were so different to everyone else, the things you talked about and the way you looked at the world. I actually missed you when you left...which was crazy, I'd only spent a few hours with you, how could I miss you? I barely knew you."
    holly "Sometimes people just get crazy feelings, it happens."
    h_haley "Not like this. You have no idea how hard my heart thumped when Paul offered me that spare room, it didn't matter that years had passed since I'd last seen you. As soon as he told me he lived with you I was sold. You were just as beautiful as I remembered, my heart was in my throat when you walked into the room that morning...I could've cried when Erin came in after you."
    holly "So could I. UwU ~"
    #haleysmile
    h_haley "Then of course came the hard part. You were so quiet and withdrawn, all I wanted was to make you smile, but it seemed like the harder I tried, the more you pulled away. Until spin the bottle...I knew you were embarrassed, mortified even, by that kiss. But that for me was the final piece of the puzzle. I knew I never wanted to kiss another soul again after that-"
    holly "But you got back with Dominic," 
    "I interrupt" 
    "why would you do that if you liked me?"
    h_haley "Well, as much as I was certain of my feelings for you, I was also kind of terrified at the idea of being in love with a woman. I mean, I liked men. I had to be sure it wasn't a phase before I tried anything with you..."
    "Then there was how you were feeling to consider. You were making such amazing progress with everything, I was worried that telling you how I felt would set you back...Bethany wasn't impressed though, she thought I was being beyond stupid." 
    holly "I can imagine, she was ready for us to get together after the whole spin the bottle thing. By the end she was nearly tearing her hair out waiting for me to see what was staring me in the face."
    h_haley "I'm really glad you eventually did come around baby." 
    "She resumes stroking my hair" 
    h_haley "You make me so happy."
    "My blush darkens and my cheeks start to burn. Haley pulls me in closer, fluttering kisses against my forehead."
    holly "You make me happy too." 
    "I reply, wrapping my arms firmly around her."
    h_haley "Good. You can go back to sleep now sweetheart."
    holly "You sure? No more burning questions?"
    h_haley "No more." 
    "She whispers as my eyelids start to droop" 
    h_haley "Night honey."
    holly "Night baby."
    
    "..."

    "Leaving Haley the next day took some serious effort. I was awake early despite being woken up at five am and decided to put my tongue to good use. Haley woke up breathing heavily and moaning loudly, her fingers gripping the sheets tight as I brought her to orgasm before cruelly climbing out of bed and whipping the duvet from her grasp as a playful retribution for the previous night."
    "I was less amused an hour after this when she jumped on me as I was trying to leave the house, her fingers delving straight under my jeans as she pressed her body and lips to mine. As soon as I tried to slip my fingers beneath her jeans to join in the fun she pulled away, wished me a Merry Christmas and left to go to her parents."
    "After several days of exchanging varying degrees of flirty and suggestive text messages our reunion on New Year's Eve was simply a blur of pleasurable ecstasy!"

    title "Final Session"

    "January 18th."
    "The day of my last session with Blaire."
    "I roll over and look at the clock, it's barely seven. I let out a heavy breath and Haley shuffles closer, wrapping her arm around my waist."

    h_haley "You can't sleep?" 
    "She mumbles sleepily."
    holly "No." 
    holly "I've been pretty restless all night; I feel kind of strange."
    h_haley "I know," 
    "She kisses my shoulder" 
    h_haley "you've barely stopped shuffling all night."
    holly "Sorry, did I keep you awake?"
    h_haley "It's ok baby, you're bound to be nervous about today. You've been seeing Blaire for a long time now, it's going to feel different knowing that after this you won't see her again. But we're all here for you, we all love you to bits, and you know you can tell any of us anything. We jus-"
    "I turn over, wrap my arms around her and hold her tight, she stiffens slightly in surprise."
    holly "I love you Haley. So, so, so much."
    h_haley "I love you too Holly." 
    "She kisses my cheek and I feel her body relax" 
    h_haley "Whatever happens, you've got this, ok?"
    holly "Ok." 
    "I smile, pressing my lips to hers as her fingers start edging the bottom of my t-shirt up around my hips."
    holly "What're you doing?" 
    "I ask, a politely puzzled expression on my face."
    h_haley "We're home alone," 
    "She giggles" 
    "I'm distracting you from your thoughts and helping you relax..."
    "She slips my t-shirt over my head and begins sucking gently on my nipples as she runs her fingernails lightly up and down my sides. I run my fingers through her hair and relax back against my pillows."

    "..."
    "It hadn't taken long for Haley to memorize the way I most enjoyed being touched and she was doing an incredible job once again, she nipped the underside of my breast as her fingers journeyed up the inside of my thigh and under my shorts."
    h_haley "You're so wet already baby." 
    "She whispers against my ear, planting kisses across my jaw" 
    h_haley "What do you fancy this morning? My fingers?" 
    "She taps her fingertips on my clit causing me to jump a little" 
    h_haley "My tongue?" 
    She presses her lips to mine and slides her tongue over my lower lip before slipping it into my mouth 
    h_haley "Or maybe something a little...bigger?" 
    "She raises an eyebrow at me while I mull over my options."
    holly "Hmmm..." 
    "I muse as she pushes a finger into my waiting pussy" 
    holly "may- maybe something we can share?"
    h_haley "Yeah?" 
    "She asks with a grin as she slips a second finger inside and curls them ever so slightly upwards."
    holly "Mmmm..." 
    "I moan, my eyes rolling back as Haley kisses my neck and increases the pace at which her fingers slide in and out of my now sopping wet pussy" 
    holly "that's so fucking good baby!"
    "I slide down in the bed and push my hands up under my pillow, my legs twitching as my orgasm rapidly approaches. Haley curls her fingers deliberately tighter and presses her thumb to my clit."
    holly "Fuck!" 
    "I jerk against her" 
    holly "Oh fuck Haley...yes...yes...God...right there!"
    "She abruptly sits up and quickly pulls her clothes off, her cheeks flush with excitement while I stare incredulously at her."
    holly "What are you doing?" 
    "I ask in disbelief."
    h_haley "Stop talking Holly." 
    "She pants, pulling me into a sitting position and lifting one of her legs over mine."
    "I quickly take the initiative and pull her in for a kiss as she edges her pussy closer."
    h_haley "Oh God Holly..." 
    "She moans loudly when our pussies meet" 
    h_haley "this feels so good! You're so wet baby..."
    "I use my free hand to play with her breasts as she rocks her hips in time with mine, our pussies sliding easily against each other's as the room fills with the sound of our combined heavy breathing."
    holly "Fuck Haley. Where did you get this idea from?"
    h_haley "I...did...some...re- research. Oh fuck, fuck baby...baby I'm gonna cum!" 
    "She grips the back of my neck hard and kisses me passionately."
    "I grip her hips firmly and rock her in time with me."
    h_haley "Jesus Holly!" 
    "She cries" 
    h_haley "Oh fuck that's good...right there baby...right there...Hoooollllyyy..."
    "She calls out my name over and over again, driving us both to such an intense orgasm that it's a good ten minutes before either of us are capable of coherent speech again."
    holly "So..." 
    "I breathe" 
    holly "What sort of 'research' did you do to come up with that one?"
    "She turns to face me and I push her sweaty fringe out of her eyes."
    holly "Don't tell me you succumbed to porn?" 
    "I ask mockingly."
    h_haley "No!" 
    "She says firmly" 
    h_haley "I asked Google for tips on lesbian sex...you'd be surprised what's out there." 
    "She winks at me and proceeds to giggle at the surprised look on my face."
    holly "Wow...that's some serious effort right there."
    h_haley "You're worth it sweetheart." 
    "She flashes me a smile and kisses me" 
    h_haley "Now..." 
    "She moves closer and wraps herself around me" 
    h_haley "You ready to face the day?"
    holly "If I say no, do I get to see what else you've got up your sleeve?"
    h_haley "Hmmm...nope!" 
    "She sticks her tongue out and playfully licks my cheek."
    holly "Gross." 
    "I giggle."
    h_haley "So gross," 
    "She smiles" 
    h_haley "You best get in the shower to get that off...I could help you if you like?" 
    "She pinches my nipple and bites her bottom lip as she looks up at me."
    holly "I think you'd better, I'm feeling far too feeble to be able to do it myself..." 
    "I grin, jumping out of bed and running to the bathroom with Haley hot on my heels."

    title "Session"

    scene bg corporate lobby small
    #show holly blaire

    h_kisaragi "So, today is our final session Holly, how are you feeling about that?" 
    "Blaire smiles at me."
    holly "Kind of uncertain." 
    "I admit."
    h_kisaragi "How so?"
    holly "Well...like..." 
    "I pause and try to find the best words to explain"
    holly "I feel like a tightrope walker who's doing one of those crazy walks over a ravine with no safety harness and no net. Everything is balanced at the moment, I'm coping with the height and everything, but one strong gust of wind and bam...I'm in the ravine...and probably dead." 
    "I add as an afterthought."
    "She laughs" 
    h_kisaragi "Perhaps don't take up tightrope walking."
    holly "I know right. I'm just scared I guess. I mean, I know if I start to really struggle again I can always come back and see you, but I've been to some dark places the past couple of years, I'm not sure I could cope with going back there again."
    h_kisaragi "Everybody has setbacks Holly." 
    "She continues as I look away to hide the grin spreading across my face" 
    h_kisaragi "I know that's my favourite saying and you're sick of hearing it, but it's the truth. I have every faith that you'll be able to survive each gust of wind life throws at you. You've made tremendous progress over the past eighteen months, you should be so proud of yourself! You have a lovely support system at home and at work. You really don't need me anymore. You can do this...yes?"
    holly "Yep," 
    "I nod and take a deep breath" 
    holly "I can do this."
    h_kisaragi "No more guilt, no more being hard on yourself and hiding your feelings from the world. Plenty of being kind to yourself and enjoying life, the good and the bad."
    holly "I promise." I smile nervously.
    h_kisaragi "Glad to hear it!" She smiles.
    holly "Thanks Blaire." 
    "I smile back" 
    holly "For everything, I couldn't have done this without you. This is for you," 
    "I reach into my bag and pass her a card" 
    holly "it's nothing much, just something to say thank you."
    h_kisaragi "Oh Holly," 
    "She stands up" 
    h_kisaragi "Thank you so much! This is so nice of you! Come on, we're skipping the breathing exercise today, give me a hug and then get yourself off home to the life you've worked so hard to live!"

    gameover "Good ending"



    #-----------------------------------------------------------------------------------------------------------------
    #Position(xpos = (placement_of(h_holly).xpos - 0.10)) with move

    scene h_bg star
    scene h_bg day
    scene h_bg dusk
    scene h_bg cloud
    scene bg corporate lobby small
    scene bg connie bedroom clean night
    scene bg connie kitchen day #/ night / evening
    scene bg sadie livingroom day 
    scene bg sadie livingroom day blur
    scene bg connie bedroom clean dark
    scene bg connie bedroom blur
    scene bg leona room dark #haleys bedroom
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