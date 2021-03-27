# Spells Known
<title>Spells Known</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<link rel="stylesheet" href="assets/css/bootstrap.css" media="screen">
<link rel="stylesheet" href="assets/css/custom.min.css">
<script type="text/javascript" async="" src="assets/js/ga.js"></script>

<script src="https://cdn.jsdelivr.net/npm/markdown-it@12.0.4/index.min.js"></script>

<script>

var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-23019901-1']);
_gaq.push(['_setDomainName', "."]);
        _gaq.push(['_setAllowLinker', true]);
      _gaq.push(['_trackPageview']);

     (function() {
       var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
       ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
       var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
     })();

    </script>

<script data-dapp-detection="">
(function() {
  let alreadyInsertedMetaTag = false

  function __insertDappDetected() {
    if (!alreadyInsertedMetaTag) {
      const meta = document.createElement('meta')
      meta.name = 'dapp-detected'
      document.head.appendChild(meta)
      alreadyInsertedMetaTag = true
    }
  }

  if (window.hasOwnProperty('web3')) {
    // Note a closure can't be used for this var because some sites like
    // www.wnyc.org do a second script execution via eval for some reason.
    window.__disableDappDetectionInsertion = true
    // Likely oldWeb3 is undefined and it has a property only because
    // we defined it. Some sites like wnyc.org are evaling all scripts
    // that exist again, so this is protection against multiple calls.
    if (window.web3 === undefined) {
      return
    }
    __insertDappDetected()
  } else {
    var oldWeb3 = window.web3
    Object.defineProperty(window, 'web3', {
      configurable: true,
      set: function (val) {
        if (!window.__disableDappDetectionInsertion)
          __insertDappDetected()
        oldWeb3 = val
      },
      get: function () {
        if (!window.__disableDappDetectionInsertion)
          __insertDappDetected()
        return oldWeb3
      }
    })
  }
})()</script>

<script>
function range() {
    var caster_level = 10
    var close_range = {25 + {{caster_level / 2} * 5}}
    document.getElementById("myText").innerHTML = close_range
}
</script>
<script>
function range() {
    var caster_level = 10;
    var close_range = {25 + {{caster_level / 2} * 5}};
    document.getElementById("myText").innerHTML = close_range
}
</script>

<span id="caster_level"></span>


<style>
    img {
        border-radius: 50%;
    }
</style>

<div id="myData"></div>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>

<script>
        fetch('./spell_full.json')
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                appendData(data);
            })
            .catch(function (err) {
                console.log('error: ' + err);
            });
        function appendData(data) {
            var mainContainer = document.getElementById("myData");
            for (var i = 0; i < data.length; i++) {
                var div = document.createElement("div");
                div.innerHTML = {'Name: ' + data[i].name + ' ' + data[i].school
            };
                mainContainer.appendChild(div);
            }
        }
</script>

<img src="https://www.dndbeyond.com/content/1-0-1487-0/skins/waterdeep/images/icons/classes/wizard.jpg" alt="Wizard">

---

## 0th level :white_circle: :white_circle: :white_circle: :white_circle: :large_blue_diamond: :large_blue_diamond: :large_blue_diamond:

<details class="card bg-light mb-3"><summary class="card-header">Prepared</summary>

### :white_circle: [Mage Hand](https://aonprd.com/SpellDisplay.aspx?ItemName=Mage%20Hand)

<details class="card border-primary mb-3"><summary class="card-header">5-pound telekinesis. <span class="badge badge-success">Transmutation</span> <span class="badge badge-pill badge-success">V</span> <span class="badge badge-pill badge-secondary">S</span> <span class="badge badge-pill badge-primary">50ft</span></summary>
<span class="card-body">

**Source** [*PRPG Core Rulebook pg. 306*](http://paizo.com/pathfinderRPG/v5748btpy88yj)\
**School** [transmutation](https://aonprd.com/SpellDefinitions.aspx?ID=8);\
**Level** arcanist 0, bard 0, magus 0, medium 0, mesmerist 0, occultist 0,
psychic 0, skald 0, sorcerer 0, spiritualist 0, summoner 0, summoner (unchained)
0, wizard 0\
**Casting Time** 1 standard action\
**Components** V, S\
**Range** close (25 ft. + 5 ft./2 levels)\
**Target** one nonmagical, unattended object weighing up to 5 lbs.\
**Duration** concentration\
**Saving Throw** none;\
**Spell Resistance** no

You point your finger at an object and can lift it and move it at will from a
distance. As a move action, you can propel the object as far as 15 feet in any
direction, though the spell ends if the distance between you and the object ever
exceeds the spell's range.

</span>

</details>

### :white_circle: [Ray of Frost](https://aonprd.com/SpellDisplay.aspx?ItemName=Ray%20of%20Frost)

<details class="card border-primary mb-3"><summary class="card-header">Ray deals 1d3 <span class="badge badge-pill badge-primary">cold</span> damage.</summary>

**Source** [*PRPG Core Rulebook pg. 330*](http://paizo.com/pathfinderRPG/v5748btpy88yj)\
**School** [evocation](https://aonprd.com/SpellDefinitions.aspx?ID=5)
[[cold](https://aonprd.com/SpellDefinitions.aspx?ID=28)]; **Level** arcanist 0,
magus 0, sorcerer 0, wizard 0
**Casting Time** 1 standard action\
**Components** V, S
**Range** close (25 ft. + 5 ft./2 levels)\
**Effect** ray\
**Duration** instantaneous\
**Saving Throw** none;\
**Spell Resistance** yes

A ray of freezing air and ice projects from your pointing finger. You must
succeed on a ranged touch attack with the ray to deal damage to a target. The
ray deals 1d3 points of cold damage.

---

</details>

### :white_circle: [Grasp](https://aonprd.com/SpellDisplay.aspx?ItemName=Grasp)

<details class="card border-primary mb-3"><summary class="card-header">Retry a Climb check as an immediate action.</summary>

**Source** [*Heroes of the Darklands pg. 9*](http://paizo.com/products/btpy9sjq)\
**School** [divination](https://aonprd.com/SpellDefinitions.aspx?ID=3); **Level** arcanist 0, bard 0, cleric 0, druid 0, hunter 0, magus 0, oracle 0, psychic 0, skald 0, sorcerer 0, warpriest 0, witch 0, wizard 0\
**Casting Time** 1 immediate action\
**Components** V\
**Range** personal\
**Target** you\
**Duration** instantaneous\
**Saving Throw** none; **Spell Resistance** no

You can cast this spell as an immediate action when you fail a Climb check and would fall. You can immediately attempt another Climb check as a free action at a --2 penalty. Each successive use of this spell in a particular situation increases the penalty by 2. If successful, you don't fall, but you don't progress at climbing.

---

</details>

### :white_circle: [Detect Fiendish Presence](https://aonprd.com/SpellDisplay.aspx?ItemName=Detect%20Fiendish%20Presence)

<details class="card border-primary mb-3"><summary class="card-header">As detect evil, except this specifically detects outsiders with the evil subtype and their servants.</summary>

**Source** [*Agents of Evil pg. 16*](http://paizo.com/products/btpy9he0?Pathfinder-Player-Companion-Agents-of-Evil)\
**School** [divination](https://aonprd.com/SpellDefinitions.aspx?ID=3); **Level** arcanist 0, bard 0, cleric 0, magus 0, oracle 0, skald 0, sorcerer 0, warpriest 0, witch 0, wizard 0
**Casting Time** 1 standard action\
**Components** V, S
**Range** 60 ft.\
**Area** cone-shaped emanation\
**Duration** concentration, up to 10 minutes/level (D)\
**Saving Throw** none; **Spell Resistance** no

This spell functions like *detect evil*, except that it detects only outsiders with the evil subtype, as well as the lingering effects caused by their gifts, presence, and spells. It can also detect clerics and paladins of fiendish deities, including Asmodeus, archdevils, daemonic harbingers, and demon lords.

---

</details>

### :large_blue_diamond: [Read Magic](https://aonprd.com/SpellDisplay.aspx?ItemName=Read%20Magic) [Staff]

<details class="card border-primary mb-3"><summary class="card-header">Read scrolls and spellbooks.</summary>

**Source** [*PRPG Core Rulebook pg. 330*](http://paizo.com/pathfinderRPG/v5748btpy88yj)\
**School** [divination](https://aonprd.com/SpellDefinitions.aspx?ID=3); **Level** adept 0, antipaladin 1, arcanist 0, bard 0, cleric 0, druid 0, hunter 0, inquisitor 0, magus 0, medium 0, mesmerist 0, occultist 0, oracle 0, paladin 1, psychic 0, ranger 1, shaman 0, skald 0, sorcerer 0, spiritualist 0, summoner 0, summoner (unchained) 0, warpriest 0, witch 0, wizard 0
**Casting Time** 1 standard action\
**Components** V, S, F (a clear crystal or mineral prism)
**Range** personal\
**Target** you\
**Duration** 10 min./level

You can decipher magical inscriptions on objects---books, scrolls, weapons, and the like---that would otherwise be unintelligible. This deciphering does not normally invoke the magic contained in the writing, although it may do so in the case of a cursed or trapped scroll. Furthermore, once the spell is cast and you have read the magical inscription, you are thereafter able to read that particular writing without recourse to the use of *read magic*. You can read at the rate of one page (250 words) per minute. The spell allows you to identify a *glyph of warding* with a DC 13 Spellcraft check, a *greater glyph of warding* with a DC 16 Spellcraft check, or any *symbol* spell with a Spellcraft check (DC 10 + spell level).

*Read magic* can be made permanent with a *permanency* spell.

---

</details>

### :large_blue_diamond: [Prestidigitation](https://aonprd.com/SpellDisplay.aspx?ItemName=Prestidigitation) [Cloak]

<details class="card border-primary mb-3"><summary class="card-header">Performs minor tricks.</summary>

**Source** [*PRPG Core Rulebook pg. 325*](http://paizo.com/pathfinderRPG/v5748btpy88yj)\
**School** [universal](https://aonprd.com/SpellDefinitions.aspx?ID=9); **Level** arcanist 0, bard 0, magus 0, medium 0, mesmerist 0, psychic 0, skald 0, sorcerer 0, wizard 0
**Casting Time** 1 standard action\
**Components** V, S
**Range** 10 ft.\
**Target, Effect, or Area** see text\
**Duration** 1 hour\
**Saving Throw** see text; **Spell Resistance** no

Prestidigitations are minor tricks that novice spellcasters use for practice. Once cast, a *prestidigitation* spell enables you to perform simple magical effects for 1 hour. The effects are minor and have severe limitations. A prestidigitation can slowly lift 1 pound of material. It can color, clean, or soil items in a 1-foot cube each round. It can chill, warm, or flavor 1 pound of nonliving material. It cannot deal damage or affect the concentration of spellcasters. *Prestidigitation* can create small objects, but they look crude and artificial. The materials created by a *prestidigitation* spell are extremely fragile, and they cannot be used as tools, weapons, or spell components. Finally, *prestidigitation* lacks the power to duplicate any other spell effects. Any actual change to an object (beyond just moving, cleaning, or soiling it) persists only 1 hour.

---

</details>

### :large_blue_diamond: [Detect Magic](https://aonprd.com/SpellDisplay.aspx?ItemName=Detect%20Magic) [Cloak]

<details class="card border-primary mb-3"><summary class="card-header">Detects spells and magic items within 60 ft.</summary>

**Source** [*PRPG Core Rulebook pg. 267*](http://paizo.com/pathfinderRPG/v5748btpy88yj)\
**School** [divination](https://aonprd.com/SpellDefinitions.aspx?ID=3); **Level** adept 0, arcanist 0, bard 0, cleric 0, druid 0, hunter 0, inquisitor 0, magus 0, medium 0, mesmerist 0, occultist 0, oracle 0, psychic 0, shaman 0, skald 0, sorcerer 0, spiritualist 0, summoner 0, summoner (unchained) 0, warpriest 0, witch 0, wizard 0
**Casting Time** 1 standard action\
**Components** V, S
**Range** 60 ft.\
**Area** cone-shaped emanation\
**Duration** concentration, up to 1 min./level (D)\
**Saving Throw** none; **Spell Resistance** no

You detect magical auras. The amount of information revealed depends on how long you study a particular area or subject.

*1st Round*: Presence or absence of magical auras.

*2nd Round*: Number of different magical auras and the power of the most potent aura.

*3rd Round*: The strength and location of each aura. If the items or creatures bearing the auras are in line of sight, you can make Knowledge (arcana) skill checks to determine the school of magic involved in each. (Make one check per aura: DC 15 + spell level, or 15 + 1/2 caster level for a nonspell effect.) If the aura eminates from a magic item, you can attempt to identify its properties (see Spellcraft).

Magical areas, multiple types of magic, or strong local magical emanations may distort or conceal weaker auras.

*Aura Strength*: An aura's power depends on a spell's functioning spell level or an item's caster level; see the accompanying table. If an aura falls into more than one category, *detect magic* indicates the stronger of the two.

*Lingering Aura*: A magical aura lingers after its original source dissipates (in the case of a spell) or is destroyed (in the case of a magic item). If detect magic is cast and directed at such a location, the spell indicates an aura strength of dim (even weaker than a faint aura). How long the aura lingers at this dim level depends on its original power:

| **Original Strength** | **Duration of Lingering Aura** |\
| Faint | 1d6 rounds |\
| Moderate | 1d6 minutes |\
| Strong | 1d6 x 10 minutes |\
| Overwhelming | 1d6 days |

Outsiders and elementals are not magical in themselves, but if they are summoned, the conjuration spell registers. Each round, you can turn to detect magic in a new area. The spell can penetrate barriers, but 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt blocks it.

*Detect magic* can be made permanent with a *permanency* spell.

| **Spell or Object** | **Aura Power** |\
| **Faint** | **Moderate** | **Strong** | **Overwhelming** |\
| Functioning spell (spell level) | 3rd or lower | 4th-6th | 7th-9th | 10th+ (deity-level) |\
| Magic item (caster level) | 5th or lower | 6th-11th | 12th-20th | 21st+ (artifact) |

---

</details>

</details>

---

## 1st level :white_circle: :white_circle: :white_circle: :white_circle: :black_circle: :black_circle: :o: :large_orange_diamond: :large_blue_diamond: :large_blue_diamond: :large_blue_diamond:

<details class="card bg-light mb-3"><summary class="card-header">Prepared</summary>

### :white_circle: [Stone Shield](https://aonprd.com/SpellDisplay.aspx?ItemName=Stone%20Shield)

<details class="card border-primary mb-3"><summary class="card-header">Summon a thick stone slab from the ground to shield you from attacks.</summary>

**Source** [*Advanced Race Guide pg. 149*](http://paizo.com/products/btpy8rv2?Pathfinder-Roleplaying-Game-Advanced-Race-Guide)\
**School** [conjuration](https://aonprd.com/SpellDefinitions.aspx?ID=2) ([creation](https://aonprd.com/SpellDefinitions.aspx?ID=13)) [[earth](https://aonprd.com/SpellDefinitions.aspx?ID=34)]; **Level** arcanist 1, bloodrager 1, cleric 1, druid 1, hunter 1, magus 2, oracle 1, shaman 1, sorcerer 1, summoner 1, summoner (unchained) 1, warpriest 1, wizard 1 (oread)
**Casting Time** 1 immediate action\
**Components** V, S, DF
**Range** 0 ft.\
**Effect** stone wall whose area is one 5-ft. square\
**Duration** 1 round\
**Saving Throw** none; **Spell Resistance** no

A 1-inch-thick slab of stone springs up from the ground, interposing itself between you and an opponent of your choice. The *stone shield* provides you with cover from that enemy until the beginning of your next turn, granting you a +4 bonus to Armor Class and a +2 bonus on Reflex saving throws. If the opponent's attack misses you by 4 or less, the attack strikes the shield instead. The *stone shield* has hardness 8 and 15 hit points. If the shield is destroyed, the spell ends and the shield crumbles away into nothingness. Spells and effects that damage an area deal damage to the shield.

You cannot use this spell if you are not adjacent to a large area of earth or stone such as the ground or a wall.

---

</details>

### :white_circle: [Wave Shield](https://aonprd.com/SpellDisplay.aspx?ItemName=Wave%20Shield)

<details class="card border-primary mb-3"><summary class="card-header">Water blunts one incoming attack or fire effect.</summary>

**Source** [*Advanced Class Guide pg. 199*](http://paizo.com/products/btpy978v?Pathfinder-Roleplaying-Game-Advanced-Class-Guide)\
**School** [abjuration](https://aonprd.com/SpellDefinitions.aspx?ID=1) [[water](https://aonprd.com/SpellDefinitions.aspx?ID=52)]; **Level** arcanist 1, bloodrager 1, druid 1, hunter 1, magus 1, shaman 1, sorcerer 1, witch 1, wizard 1
**Casting Time** 1 immediate action\
**Components** V
**Range** personal\
**Target** you\
**Duration** 1 round or until discharged

You create a rushing torrent of water in the rough outline of a shield. The water protects you from one physical or fire attack, granting you DR/--- and fire resistance equal to half your caster level (minimum 1) on that attack. Once the spell has reduced the damage of one attack against you, it is discharged.

---

</details>

### :white_circle: [Air Bubble](https://aonprd.com/SpellDisplay.aspx?ItemName=Air%20Bubble)

<details class="card border-primary mb-3"><summary class="card-header">Creates a small pocket of air around your head or an object.</summary>

**Source** [*Ultimate Combat pg. 222*](http://paizo.com/pathfinderRPG/v5748btpy8mcz)\
**School** [conjuration](https://aonprd.com/SpellDefinitions.aspx?ID=2) ([creation](https://aonprd.com/SpellDefinitions.aspx?ID=13)); **Level** arcanist 1, cleric 1, druid 1, hunter 1, oracle 1, psychic 1, ranger 1, sorcerer 1, warpriest 1, witch 1, wizard 1
**Casting Time** 1 standard action\
**Components** S, M/DF (a small bladder filled with air)
**Range** touch\
**Target** one creature or one object no larger than a Large two-handed weapon\
**Duration** 1 minute/level\
**Saving Throw** Will negates (harmless); **Spell Resistance** yes (harmless)

*Air bubble* creates a small pocket of breathable air that surrounds the touched creature's head or the touched object. The air bubble allows the creature touched to breathe underwater or in similar airless environments, or protects the object touched from water damage.

A firearm within an *air bubble* can be loaded---assuming the black powder comes from a powder horn, a cartridge, or some other airtight protective device---and fired. When shooting such a firearm underwater, the shot still takes the standard --2 penalty on attack rolls for every 5 feet of water the bullet passes through, in addition to normal penalties due to range. If a firearm within the *air bubble* explodes, the explosion occurs normally.

---

</details>

### :white_circle: [Protection From Evil](https://aonprd.com/SpellDisplay.aspx?ItemName=Protection%20from%20Evil)

<details class="card border-primary mb-3"><summary class="card-header">+2 to AC and saves, plus additional protection against selected alignment.</summary>

**Source** [*PRPG Core Rulebook pg. 327*](http://paizo.com/pathfinderRPG/v5748btpy88yj)\
**School** [abjuration](https://aonprd.com/SpellDefinitions.aspx?ID=1) [[good](https://aonprd.com/SpellDefinitions.aspx?ID=41)]; **Level** adept 1, arcanist 1, bloodrager 1, cleric 1, inquisitor 1, medium 1, oracle 1, paladin 1, shaman 1, sorcerer 1, spiritualist 1, summoner 1, summoner (unchained) 1, warpriest 1, wizard 1
**Casting Time** 1 standard action\
**Components** V, S, M/DF
**Range** touch\
**Target** creature touched\
**Duration** 1 min./level (D)\
**Saving Throw** Will negates (harmless); **Spell Resistance** no; see text

This spell wards a creature from attacks by evil creatures, from mental control, and from summoned creatures. It creates a magical barrier around the subject at a distance of 1 foot. The barrier moves with the subject and has three major effects.

First, the subject gains a +2 deflection bonus to AC and a +2 resistance bonus on saves. Both these bonuses apply against attacks made or effects created by evil creatures.

Second, the subject immediately receives another saving throw (if one was allowed to begin with) against any spells or effects that possess or exercise mental control over the creature (including enchantment [charm] effects and enchantment [compulsion] effects, such as *charm person*, *command*, and *dominate person*. This saving throw is made with a +2 morale bonus, using the same DC as the original effect. If successful, such effects are suppressed for the duration of this spell. The effects resume when the duration of this spell expires. While under the effects of this spell, the target is immune to any new attempts to possess or exercise mental control over the target. This spell does not expel a controlling life force (such as a ghost or spellcaster using *magic jar*), but it does prevent them from controlling the target. This second effect only functions against spells and effects created by evil creatures or objects, subject to GM discretion.

Third, the spell prevents bodily contact by evil summoned creatures. This causes the natural weapon attacks of such creatures to fail and the creatures to recoil if such attacks require touching the warded creature. Summoned creatures that are not evil are immune to this effect. The protection against contact by summoned creatures ends if the warded creature makes an attack against or tries to force the barrier against the blocked creature. Spell resistance can allow a creature to overcome this protection and touch the warded creature.

---

</details>

### :black_circle: [Heightened Awareness](https://aonprd.com/SpellDisplay.aspx?ItemName=Heightened%20Awareness)

<details class="card border-primary mb-3"><summary class="card-header">Your recall and ability to process information improve.</summary>

**Source** [*Advanced Class Guide pg. 183*](http://paizo.com/products/btpy978v?Pathfinder-Roleplaying-Game-Advanced-Class-Guide)\
**School** [divination](https://aonprd.com/SpellDefinitions.aspx?ID=3); **Level** alchemist 1, arcanist 1, bard 1, druid 1, hunter 1, inquisitor 1, investigator 1, medium 1, mesmerist 1, occultist 1, psychic 1, ranger 1, shaman 1, skald 1, sorcerer 1, wizard 1
**Casting Time** 1 standard action\
**Components** V, M/DF (a coffee bean)
**Range** personal\
**Target** you\
**Duration** 10 minutes/level (D)

You enter a heightened state of awareness that allows you to notice more about your surroundings and recall information effortlessly. You gain a +2 competence bonus on Perception checks and on all Knowledge checks that you are trained in.

If this spell is active when you have to make an initiative check, you can instantly dismiss this spell and gain a +4 bonus on that check.

---

</details>

### :black_circle: [Mage Armor](https://aonprd.com/SpellDisplay.aspx?ItemName=Mage%20Armor)

<details class="card border-primary mb-3"><summary class="card-header">Gives subject +4 armor bonus.</summary>

**Source** [*PRPG Core Rulebook pg. 306*](http://paizo.com/pathfinderRPG/v5748btpy88yj)\
**School** [conjuration](https://aonprd.com/SpellDefinitions.aspx?ID=2) ([creation](https://aonprd.com/SpellDefinitions.aspx?ID=13)) [[force](https://aonprd.com/SpellDefinitions.aspx?ID=40)]; **Level** arcanist 1, bloodrager 1, occultist 1, psychic 1, sorcerer 1, spiritualist 1, summoner 1, summoner (unchained) 1, witch 1, wizard 1
**Casting Time** 1 standard action\
**Components** V, S, F (a piece of cured leather)
**Range** touch\
**Target** creature touched\
**Duration** 1 hour/level (D)\
**Saving Throw** Will negates (harmless); **Spell Resistance** no

An invisible but tangible field of force surrounds the subject of a *mage armor* spell, providing a +4 armor bonus to AC.

Unlike mundane armor, *mage armor* entails no armor check penalty, arcane spell failure chance, or speed reduction. Since *mage armor* is made of force, incorporeal creatures can't bypass it the way they do normal armor.

---

</details>

### :o: [Pearl](https://aonprd.com/MagicWondrousDisplay.aspx?FinalName=Pearl%20of%20Power1st) 1st

<details class="card border-primary mb-3"><summary class="card-header">Once per day, recall any one spell.</summary>

**Source** [*Ultimate Equipment pg. 315*](http://paizo.com/products/btpy8tmc?Pathfinder-Roleplaying-Game-Ultimate-Equipment), [*PRPG Core Rulebook pg. 525*](http://paizo.com/pathfinderRPG/v5748btpy88yj)\
**Aura** strong transmutation; **CL** 17th\
**Slot** none; **Price** 1,000 gp (![](https://aonprd.com/images/PathfinderSocietySymbol.gif "PFS Legal") 1st), 4,000 gp (![](https://aonprd.com/images/PathfinderSocietySymbol.gif "PFS Legal") 2nd), 9,000 gp (![](https://aonprd.com/images/PathfinderSocietySymbol.gif "PFS Legal") 3rd), 16,000 gp (![](https://aonprd.com/images/PathfinderSocietySymbol.gif "PFS Legal") 4th), 25,000 gp (![](https://aonprd.com/images/PathfinderSocietySymbol.gif "PFS Legal") 5th), 36,000 gp (![](https://aonprd.com/images/PathfinderSocietySymbol.gif "PFS Legal") 6th), 49,000 gp (![](https://aonprd.com/images/PathfinderSocietySymbol.gif "PFS Legal") 7th), 64,000 gp (![](https://aonprd.com/images/PathfinderSocietySymbol.gif "PFS Legal") 8th), 70,000 gp (![](https://aonprd.com/images/PathfinderSocietySymbol.gif "PFS Legal") Two Spells), 81,000 gp (![](https://aonprd.com/images/PathfinderSocietySymbol.gif "PFS Legal") 9th); **Weight** ---

This seemingly normal pearl of average size and luster is a potent aid to all spellcasters who prepare spells. Once per day on command, a *pearl of power* enables the possessor to recall any one spell that she had prepared and then cast that day. The spell is then prepared again, just as if it had not been cast. The spell must be of a particular level, depending on the pearl. Different pearls exist for recalling one spell per day of each level from 1st through 9th and for the recall of two spells per day (each of a different level, 6th or lower).

**Requirements** Craft Wondrous Item, creator must be able to cast spells of the spell level to be recalled; **Cost** 500 gp (1st), 2,000 gp (2nd), 4,500 gp (3rd), 8,000 gp (4th), 12,500 gp (5th), 18,000 gp (6th), 24,500 gp (7th), 32,000 gp (8th), 35,000 gp (Two Spells), 40,500 gp (9th)

---

</details>

### :large_orange_diamond: [Shield](https://aonprd.com/SpellDisplay.aspx?ItemName=Shield) [Staff]

<details class="card border-primary mb-3"><summary class="card-header">Invisible disc gives +4 to AC, blocks magic missiles.</summary>

**Source** [*PRPG Core Rulebook pg. 342*](http://paizo.com/pathfinderRPG/v5748btpy88yj)\
**School** [abjuration](https://aonprd.com/SpellDefinitions.aspx?ID=1) [[force](https://aonprd.com/SpellDefinitions.aspx?ID=40)]; **Level** alchemist 1, arcanist 1, bloodrager 1, investigator 1, magus 1, occultist 1, psychic 1, sorcerer 1, spiritualist 1, summoner 1, summoner (unchained) 1, wizard 1
**Casting Time** 1 standard action\
**Components** V, S
**Range** personal\
**Target** you\
**Duration** 1 min./level (D)

*Shield* creates an invisible shield of force that hovers in front of you. It negates *magic missile* attacks directed at you. The disk also provides a +4 shield bonus to AC. This bonus applies against incorporeal touch attacks, since it is a force effect. The *shield* has no armor check penalty or arcane spell failure chance.

---

</details>

### :large_blue_diamond: [Magic Missile](https://aonprd.com/SpellDisplay.aspx?ItemName=Magic%20Missile) [Staff]

<details class="card border-primary mb-3"><summary class="card-header">1d4+1 damage; +1 missile per two levels above 1st (max 5).</summary>

**Source** [*PRPG Core Rulebook pg. 309*](http://paizo.com/pathfinderRPG/v5748btpy88yj)\
**School** [evocation](https://aonprd.com/SpellDefinitions.aspx?ID=5) [[force](https://aonprd.com/SpellDefinitions.aspx?ID=40)]; **Level** arcanist 1, bloodrager 1, magus 1, psychic 1, sorcerer 1, wizard 1
**Casting Time** 1 standard action\
**Components** V, S
**Range** medium (100 ft. + 10 ft./level)\
**Targets** up to five creatures, no two of which can be more than 15 ft. apart\
**Duration** instantaneous\
**Saving Throw** none; **Spell Resistance** yes

A missile of magical energy darts forth from your fingertip and strikes its target, dealing 1d4+1 points of force damage.

The missile strikes unerringly, even if the target is in melee combat, so long as it has less than total cover or total concealment. Specific parts of a creature can't be singled out. Objects are not damaged by the spell.

For every two caster levels beyond 1st, you gain an additional missile---two at 3rd level, three at 5th, four at 7th, and the maximum of five missiles at 9th level or higher. If you shoot multiple missiles, you can have them strike a single creature or several creatures. A single missile can strike only one creature. You must designate targets before you check for spell resistance or roll damage.

---

</details>

### :large_blue_diamond: [Detect Secret Doors](https://aonprd.com/SpellDisplay.aspx?ItemName=Detect%20Secret%20Doors) [Cloak]

<details class="card border-primary mb-3"><summary class="card-header">Reveals hidden doors within 60 ft.</summary>

**Source** [*PRPG Core Rulebook pg. 268*](http://paizo.com/pathfinderRPG/v5748btpy88yj)\
**School** [divination](https://aonprd.com/SpellDefinitions.aspx?ID=3); **Level** alchemist 1, arcanist 1, bard 1, investigator 1, mesmerist 1, occultist 1, psychic 1, skald 1, sorcerer 1, witch 1, wizard 1
**Casting Time** 1 standard action\
**Components** V, S
**Range** 60 ft.\
**Area** cone-shaped emanation\
**Duration** concentration, up to 1 min./level (D)\
**Saving Throw** none; **Spell Resistance** no

You can detect secret doors, compartments, caches, and so forth. Only passages, doors, or openings that have been specifically constructed to escape detection are detected by this spell. The amount of information revealed depends on how long you study a particular area or subject.

*1st Round*: Presence or absence of secret doors.

*2nd Round*: Number of secret doors and the location of each. If an aura is outside your line of sight, then you discern its direction but not its exact location.

*Each Additional Round*: The mechanism or trigger for one particular secret portal closely examined by you. Each round, you can turn to detect secret doors in a new area. The spell can penetrate barriers, but 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt blocks it.

---

</details>

### :large_blue_diamond: [True Strike](https://aonprd.com/SpellDisplay.aspx?ItemName=True%20Strike) [Cloak]

<details class="card border-primary mb-3"><summary class="card-header">+20 on your next attack roll.</summary>

**Source** [*PRPG Core Rulebook pg. 363*](http://paizo.com/pathfinderRPG/v5748btpy88yj)\
**School** [divination](https://aonprd.com/SpellDefinitions.aspx?ID=3); **Level** alchemist 1, arcanist 1, bloodrager 1, inquisitor 1, investigator 1, magus 1, medium 1, psychic 1, sorcerer 1, wizard 1
**Casting Time** 1 standard action\
**Components** V, F (small wooden replica of an archery target)
**Range** personal\
**Target** you\
**Duration** see text

You gain temporary, intuitive insight into the immediate future during your next attack. Your next single attack roll (if it is made before the end of the next round) gains a +20 insight bonus. Additionally, you are not affected by the miss chance that applies to attackers trying to strike a concealed target.

---

</details>

</details>

---

</details>

## 2nd level :white_circle: :black_circle: :black_circle: :black_circle: :black_circle: :black_circle: :large_orange_diamond:

<details class="card bg-light mb-3"><summary class="card-header">Prepared</summary>

### :white_circle: [Admonishing Ray](https://aonprd.com/SpellDisplay.aspx?ItemName=Admonishing%20Ray) [Maximize] 12*6 = 72

<details class="card border-primary mb-3"><summary class="card-header">Fire multiple rays that deal nonlethal force.</summary>

**Source** [*Taldor, Echoes of Glory pg. 24*](http://paizo.com/store/downloads/pathfinder/pathfinderCompanion/35E/v5748btpy8853)\
**School** [evocation](https://aonprd.com/SpellDefinitions.aspx?ID=5) [[force](https://aonprd.com/SpellDefinitions.aspx?ID=40)]; **Level** arcanist 2, cleric 2, oracle 2, sorcerer 2, warpriest 2, wizard 2
**Casting Time** 1 standard action\
**Components** V, S
**Range** close (25 ft. + 5 ft./2 levels)\
**Effect** one or more rays\
**Duration** instantaneous\
**Saving Throw** none; **Spell Resistance** yes

You blast your enemies with rays of nonlethal force. You may fire one ray, plus one additional ray for every four levels you possess beyond 3rd (to a maximum of three rays at 11th level). Each ray requires a ranged touch attack to hit and deals 4d6 points of nonlethal damage. This is a force effect. The rays may be fired at the same or different targets, but all rays must be fired simultaneously and aimed at targets within 30 feet of each other. The rays hit about as hard as a punch from a strong adult human, and can knock away unattended objects weighing up to 10 pounds if that amount of force could normally do so.

---

</details>

### :black_circle: [Fox's Cunning](https://aonprd.com/SpellDisplay.aspx?ItemName=Fox%27s%20Cunning) [Bear's Endurance]

<details class="card border-primary mb-3"><summary class="card-header">Subject gains +4 to Int for 1 min./level.</summary>

**Source** [*PRPG Core Rulebook pg. 286*](http://paizo.com/pathfinderRPG/v5748btpy88yj)\
**School** [transmutation](https://aonprd.com/SpellDefinitions.aspx?ID=8); **Level** alchemist 2, arcanist 2, bard 2, investigator 2, medium 2, psychic 2, redmantisassassin 2, skald 2, sorcerer 2, summoner 2, summoner (unchained) 2, wizard 2
**Casting Time** 1 standard action\
**Components** V, S, M/DF (hairs or dung from a fox)
**Range** touch\
**Target** you\
**Duration** 1 min./level\
**Saving Throw** Will negates (harmless); **Spell Resistance** yes

The target becomes smarter. The spell grants a +4 enhancement bonus to Intelligence, adding the usual benefits to Intelligence-based skill checks and other uses of the Intelligence modifier. Wizards (and other spellcasters who rely on Intelligence) affected by this spell do not gain any additional bonus spells for the increased Intelligence, but the save DCs for spells they cast while under this spell's effect do increase. This spell doesn't grant extra skill ranks.

---

</details>

### :black_circle: [See Invisibility](https://aonprd.com/SpellDisplay.aspx?ItemName=See%20Invisibility)

<details class="card border-primary mb-3"><summary class="card-header">Reveals invisible creatures or objects.</summary>

**Source** [*PRPG Core Rulebook pg. 339*](http://paizo.com/pathfinderRPG/v5748btpy88yj)\
**School** [divination](https://aonprd.com/SpellDefinitions.aspx?ID=3); **Level** adept 2, alchemist 2, arcanist 2, bard 3, bloodrager 2, inquisitor 2, investigator 2, mesmerist 3, occultist 2, psychic 2, skald 3, sorcerer 2, spiritualist 2, summoner 2, summoner (unchained) 2, witch 2, wizard 2
**Casting Time** 1 standard action\
**Components** V, S, M (talc and powdered silver)
**Range** personal\
**Target** you\
**Duration** 10 min./level (D)

You can see any objects or beings that are invisible within your range of vision, as well as any that are ethereal, as if they were normally visible. Such creatures are visible to you as translucent shapes, allowing you easily to discern the difference between visible, invisible, and ethereal creatures.

The spell does not reveal the method used to obtain invisibility. It does not reveal illusions or enable you to see through opaque objects. It does not reveal creatures who are simply hiding, concealed, or otherwise hard to see.

*See invisibility* can be made permanent with a *permanency* spell.

---

</details>

### :black_circle: [False Life](https://aonprd.com/SpellDisplay.aspx?ItemName=False%20Life) (Mythic)

<details class="card border-primary mb-3"><summary class="card-header">Gain 1d10 temporary hp + 1/level (max +10). Mythic increases to 2d8 + 2 per caster level (maximum +20).</summary>

**Source** [*PRPG Core Rulebook pg. 280*](http://paizo.com/pathfinderRPG/v5748btpy88yj)\
**School** [necromancy](https://aonprd.com/SpellDefinitions.aspx?ID=7); **Level** alchemist 2, arcanist 2, bloodrager 2, investigator 2, medium 2, mesmerist 2, occultist 2, psychic 2, shaman 2, sorcerer 2, spiritualist 2, witch 2, wizard 2
**Casting Time** 1 standard action\
**Components** V, S, M (a drop of blood)
**Range** personal\
**Target** you\
**Duration** 1 hour/level or until discharged; see text

You harness the power of unlife to grant yourself a limited ability to avoid death. While this spell is in effect, you gain temporary hit points equal to 1d10 + 1 per caster level (maximum +10).

Mythic False Life

**Source** [*Mythic Adventures pg. 93*](http://paizo.com/products/btpy8ywe?Pathfinder-Roleplaying-Game-Mythic-Adventures)\
The temporary hit points gained increase to 2d8 + 2 per caster level (maximum +20). As an immediate action, you can dismiss the remaining duration of the spell to prevent 1 point of Strength, Dexterity, or Constitution damage per 10 temporary hit points remaining from the spell. This takes effect after the attack hits you and the damage is rolled, but before you take the damage. For example, if you have 22 temporary hit points from *mythic false life* and a wyvern stings you for 3 points of Constitution damage, you can dismiss the spell to prevent 2 points of Constitution damage from that attack.

---

</details>

### :black_circle: [False Life](https://aonprd.com/SpellDisplay.aspx?ItemName=False%20Life) (Mythic) 2

<details class="card border-primary mb-3"><summary class="card-header">Gain 1d10 temporary hp + 1/level (max +10). Mythic increases to 2d8 + 2 per caster level (maximum +20).</summary>

Gain 1d10 temporary hp + 1/level (max +10). Mythic increases to 2d8 + 2 per caster level (maximum +20).

---

</details>

### :black_circle: [Protection From Arrows](https://aonprd.com/SpellDisplay.aspx?ItemName=Protection%20from%20Arrows)

<details class="card border-primary mb-3"><summary class="card-header">Subject gains DR 10/magic against ranged attacks.</summary>

**Source** [*PRPG Core Rulebook pg. 327*](http://paizo.com/pathfinderRPG/v5748btpy88yj)\
**School** [abjuration](https://aonprd.com/SpellDefinitions.aspx?ID=1); **Level** alchemist 2, arcanist 2, bloodrager 2, investigator 2, psychic 2, sorcerer 2, spiritualist 2, summoner 2, summoner (unchained) 2, wizard 2
**Casting Time** 1 standard action\
**Components** V, S, F (a piece of tortoiseshell or turtle shell)
**Range** touch\
**Target** creature touched\
**Duration** 1 hour/level or until discharged\
**Saving Throw** Will negates (harmless); **Spell Resistance** yes (harmless)

The warded creature gains resistance to ranged weapons. The subject gains damage reduction 10/magic against ranged weapons. This spell doesn't grant you the ability to damage creatures with similar damage reduction. Once the spell has prevented a total of 10 points of damage per caster level (maximum 100 points), it is discharged.

---

</details>

### :large_orange_diamond: [Mirror Image](https://aonprd.com/SpellDisplay.aspx?ItemName=Mirror%20Image) [Wand]

<details class="card border-primary mb-3"><summary class="card-header">Creates decoy duplicates of you (1d4 + 1 per three levels, max 8).</summary>

**Source** [*PRPG Core Rulebook pg. 314*](http://paizo.com/pathfinderRPG/v5748btpy88yj)\
**School** [illusion](https://aonprd.com/SpellDefinitions.aspx?ID=6) ([figment](https://aonprd.com/SpellDefinitions.aspx?ID=14)); **Level** adept 2, arcanist 2, bard 2, bloodrager 2, magus 2, medium 2, mesmerist 2, occultist 2, psychic 2, redmantisassassin 2, skald 2, sorcerer 2, wizard 2
**Casting Time** 1 standard action\
**Components** V, S
**Range** personal\
**Target** you\
**Duration** 1 min./level

This spell creates a number of illusory doubles of you that inhabit your square. These doubles make it difficult for enemies to precisely locate and attack you.

When *mirror image* is cast, 1d4 images plus one image per three caster levels (maximum eight images total) are created. These images remain in your space and move with you, mimicking your movements, sounds, and actions exactly. Whenever you are attacked or are the target of a spell that requires an attack roll, there is a possibility that the attack targets one of your images instead. If the attack is a hit, roll randomly to see whether the selected target is real or a figment. If it is a figment, the figment is destroyed. If the attack misses by 5 or less, one of your figments is destroyed by the near miss. Area spells affect you normally and do not destroy any of your figments. Spells and effects that do not require an attack roll affect you normally and do not destroy any of your figments. Spells that require a touch attack are harmlessly discharged if used to destroy a figment.

An attacker must be able to see the figments to be fooled. If you are invisible or the attacker is blind, the spell has no effect (although the normal miss chances still apply).

---

</details>

</details>

---

## 3rd level :white_circle: :white_circle: :white_circle: :black_circle: :black_circle: :o:

<details class="card bg-light mb-3"><summary class="card-header">Prepared</summary>

### :white_circle: [Dispel Magic](https://aonprd.com/SpellDisplay.aspx?ItemName=Dispel%20Magic)

<details class="card border-primary mb-3"><summary class="card-header">Cancels one magical spell or effect.</summary>

**Source** [*PRPG Core Rulebook pg. 314*](http://paizo.com/pathfinderRPG/v5748btpy88yj)

**School** [illusion](https://aonprd.com/SpellDefinitions.aspx?ID=6) ([figment](https://aonprd.com/SpellDefinitions.aspx?ID=14)); **Level** adept 2, arcanist 2, bard 2, bloodrager 2, magus 2, medium 2, mesmerist 2, occultist 2, psychic 2, redmantisassassin 2, skald 2, sorcerer 2, wizard 2

**Casting Time** 1 standard action

**Components** V, S

**Range** personal

**Target** you

**Duration** 1 min./level

This spell creates a number of illusory doubles of you that inhabit your square. These doubles make it difficult for enemies to precisely locate and attack you.

When *mirror image* is cast, 1d4 images plus one image per three caster levels (maximum eight images total) are created. These images remain in your space and move with you, mimicking your movements, sounds, and actions exactly. Whenever you are attacked or are the target of a spell that requires an attack roll, there is a possibility that the attack targets one of your images instead. If the attack is a hit, roll randomly to see whether the selected target is real or a figment. If it is a figment, the figment is destroyed. If the attack misses by 5 or less, one of your figments is destroyed by the near miss. Area spells affect you normally and do not destroy any of your figments. Spells and effects that do not require an attack roll affect you normally and do not destroy any of your figments. Spells that require a touch attack are harmlessly discharged if used to destroy a figment.

An attacker must be able to see the figments to be fooled. If you are invisible or the attacker is blind, the spell has no effect (although the normal miss chances still apply).

---

</details>

### :white_circle: [Blink](https://aonprd.com/SpellDisplay.aspx?ItemName=Blink)

<details class="card border-primary mb-3"><summary class="card-header">You randomly vanish and reappear for 1 round per level.</summary>

**Source** [*PRPG Core Rulebook pg. 250*](http://paizo.com/pathfinderRPG/v5748btpy88yj)\
**School** [transmutation](https://aonprd.com/SpellDefinitions.aspx?ID=8); **Level** arcanist 3, bard 3, magus 3, psychic 3, redmantisassassin 3, skald 3, sorcerer 3, wizard 3
**Casting Time** 1 standard action\
**Components** V, S
**Range** personal\
**Target** you\
**Duration** 1 round/level (D)

You "blink" quickly back and forth between the Material Plane and the Ethereal Plane and look as though you're winking in and out of reality at random. *Blink* has several effects, as follows.

Physical attacks against you have a 50% miss chance, and the Blind-Fight feat doesn't help opponents, since you're ethereal and not merely invisible. If the attack is capable of striking ethereal creatures, the miss chance is only 20% (for concealment).

If the attacker can see invisible creatures, the miss chance is also only 20%. (For an attacker who can both see and strike ethereal creatures, there is no miss chance.) Likewise, your own attacks have a 20% miss chance, since you sometimes go ethereal just as you are about to strike.

Any individually targeted spell has a 50% chance to fail against you while you're blinking unless your attacker can target invisible, ethereal creatures. Your own spells have a 20% chance to activate just as you go ethereal, in which case they typically do not affect the Material Plane (but they might affect targets on the Ethereal Plane).

While blinking, you take only half damage from area attacks (but full damage from those that extend onto the Ethereal Plane). Although you are only partially visible, you are not considered invisible and targets retain their Dexterity bonus to AC against your attacks. You do receive a +2 bonus on attack rolls made against enemies that cannot see invisible creatures.

You take only half damage from falling, since you fall only while you are material.

While blinking, you can step through (but not see through) solid objects. For each 5 feet of solid material you walk through, there is a 50% chance that you become material. If this occurs, you are shunted off to the nearest open space and take 1d6 points of damage per 5 feet so traveled.

Since you spend about half your time on the Ethereal Plane, you can see and even attack ethereal creatures. You interact with ethereal creatures roughly the same way you interact with material ones.

An ethereal creature is invisible, incorporeal, and capable of moving in any direction, even up or down. As an incorporeal creature, you can move through solid objects, including living creatures.

An ethereal creature can see and hear the Material Plane, but everything looks gray and insubstantial. Sight and hearing on the Material Plane are limited to 60 feet.

Force effects and abjurations affect you normally. Their effects extend onto the Ethereal Plane from the Material Plane, but not vice versa. An ethereal creature can't attack material creatures, and spells you cast while ethereal affect only other ethereal things. Certain material creatures or objects have attacks or effects that work on the Ethereal Plane. Treat other ethereal creatures and objects as material.

---

</details>

### :white_circle: [Greater Invisibility](https://aonprd.com/SpellDisplay.aspx?ItemName=Invisibility)

<details class="card border-primary mb-3"><summary class="card-header">As invisibility, but subject can attack and stay invisible.</summary>

**Source** [*PRPG Core Rulebook pg. 302*](http://paizo.com/pathfinderRPG/v5748btpy88yj)\
**School** [illusion](https://aonprd.com/SpellDefinitions.aspx?ID=6) ([glamer](https://aonprd.com/SpellDefinitions.aspx?ID=15)); **Level** alchemist 4, antipaladin 4, arcanist 4, bard 4, inquisitor 4, investigator 4, magus 4, medium 3, mesmerist 4, occultist 4, psychic 4, redmantisassassin 4, skald 4, sorcerer 4, spiritualist 4, summoner 3, summoner (unchained) 4, wizard 4
**Casting Time** 1 standard action\
**Components** V, S
**Range** personal or touch\
**Target** you or creature touched\
**Duration** 1 round/level (D)\
**Saving Throw** Will negates (harmless); **Spell Resistance** yes (harmless)

This spell functions like *invisibility*, except that it doesn't end if the subject attacks.

---

</details>

### :black_circle: [Ablative Barrier](https://aonprd.com/SpellDisplay.aspx?ItemName=Ablative%20Barrier)

<details class="card border-primary mb-3"><summary class="card-header">Surrounds the target with layers of force.</summary>

**Source** [*Ultimate Combat pg. 221*](http://paizo.com/pathfinderRPG/v5748btpy8mcz)\
**School** [conjuration](https://aonprd.com/SpellDefinitions.aspx?ID=2) ([creation](https://aonprd.com/SpellDefinitions.aspx?ID=13)) [[force](https://aonprd.com/SpellDefinitions.aspx?ID=40)]; **Level** alchemist 2, arcanist 3, bloodrager 2, investigator 2, magus 2, occultist 2, psychic 3, sorcerer 3, summoner 2, summoner (unchained) 3, wizard 3
**Casting Time** 1 standard action\
**Components** V, S, M (a piece of metal cut from a shield)
**Range** touch\
**Target** creature touched\
**Duration** 1 hour/level or until discharged\
**Saving Throw** Will negates (harmless); **Spell Resistance** no

Invisible layers of solid force surround and protect the target, granting that target a +2 armor bonus to AC. Additionally, the first 5 points of lethal damage the target takes from each attack are converted into nonlethal damage. Against attacks that already deal nonlethal damage, the target gains DR 5/---. Once this spell has converted 5 points of damage to nonlethal damage per caster level (maximum 50 points), the spell is discharged.

---

</details>

### :black_circle: [Countless Eyes](https://aonprd.com/SpellDisplay.aspx?ItemName=Countless%20Eyes)

<details class="card border-primary mb-3"><summary class="card-header">Extra eyes give all-around vision.</summary>

**Source** [*Ultimate Magic pg. 213*](http://paizo.com/pathfinderRPG/v5748btpy8k8r)\
**School** [transmutation](https://aonprd.com/SpellDefinitions.aspx?ID=8); **Level** alchemist 3, arcanist 3, bloodrager 3, inquisitor 3, investigator 3, occultist 3, psychic 3, redmantisassassin 3, sorcerer 3, witch 3, wizard 3
**Casting Time** 1 standard action\
**Components** V, S
**Range** touch\
**Target** creature touched\
**Duration** 1 hour/level\
**Saving Throw** Will negates (harmless); **Spell Resistance** yes (harmless)

The target sprouts extra eyes all over its body, including on the back of its head. It gains all-around vision and cannot be flanked.

---

</details>

### :o: [Pearl 3rd]

<details class="card border-primary mb-3"><summary class="card-header">Once per day, recall any one spell.</summary>

**Source** [*Ultimate Equipment pg. 315*](http://paizo.com/products/btpy8tmc?Pathfinder-Roleplaying-Game-Ultimate-Equipment), [*PRPG Core Rulebook pg. 525*](http://paizo.com/pathfinderRPG/v5748btpy88yj)\
**Aura** strong transmutation; **CL** 17th\
**Slot** none; **Price** 1,000 gp (![](https://aonprd.com/images/PathfinderSocietySymbol.gif "PFS Legal") 1st), 4,000 gp (![](https://aonprd.com/images/PathfinderSocietySymbol.gif "PFS Legal") 2nd), 9,000 gp (![](https://aonprd.com/images/PathfinderSocietySymbol.gif "PFS Legal") 3rd), 16,000 gp (![](https://aonprd.com/images/PathfinderSocietySymbol.gif "PFS Legal") 4th), 25,000 gp (![](https://aonprd.com/images/PathfinderSocietySymbol.gif "PFS Legal") 5th), 36,000 gp (![](https://aonprd.com/images/PathfinderSocietySymbol.gif "PFS Legal") 6th), 49,000 gp (![](https://aonprd.com/images/PathfinderSocietySymbol.gif "PFS Legal") 7th), 64,000 gp (![](https://aonprd.com/images/PathfinderSocietySymbol.gif "PFS Legal") 8th), 70,000 gp (![](https://aonprd.com/images/PathfinderSocietySymbol.gif "PFS Legal") Two Spells), 81,000 gp (![](https://aonprd.com/images/PathfinderSocietySymbol.gif "PFS Legal") 9th); **Weight** ---

This seemingly normal pearl of average size and luster is a potent aid to all spellcasters who prepare spells. Once per day on command, a *pearl of power* enables the possessor to recall any one spell that she had prepared and then cast that day. The spell is then prepared again, just as if it had not been cast. The spell must be of a particular level, depending on the pearl. Different pearls exist for recalling one spell per day of each level from 1st through 9th and for the recall of two spells per day (each of a different level, 6th or lower).

**Requirements** Craft Wondrous Item, creator must be able to cast spells of the spell level to be recalled; **Cost** 500 gp (1st), 2,000 gp (2nd), 4,500 gp (3rd), 8,000 gp (4th), 12,500 gp (5th), 18,000 gp (6th), 24,500 gp (7th), 32,000 gp (8th), 35,000 gp (Two Spells), 40,500 gp (9th)

---

</details>

</details>

---

## 4th level :white_circle: :white_circle: :white_circle: :white_circle: :white_circle:

<details class="card bg-light mb-3"><summary class="card-header">Prepared</summary>

### :white_circle: [Dimension Door](https://aonprd.com/SpellDisplay.aspx?ItemName=Dimension%20Door)

<details class="card border-primary mb-3"><summary class="card-header">Teleports you a short distance.</summary>

**Source** [*PRPG Core Rulebook pg. 269*](http://paizo.com/pathfinderRPG/v5748btpy88yj)\
**School** [conjuration](https://aonprd.com/SpellDefinitions.aspx?ID=2) ([teleportation](https://aonprd.com/SpellDefinitions.aspx?ID=24)); **Level** arcanist 4, bard 4, magus 4, medium 3, mesmerist 4, occultist 4, psychic 4, skald 4, sorcerer 4, spiritualist 4, summoner 3, summoner (unchained) 4, witch 4, wizard 4
**Casting Time** 1 standard action\
**Components** V
**Range** long (400 ft. + 40 ft./level)\
**Target** you and touched objects or other touched willing creatures\
**Duration** instantaneous\
**Saving Throw** none and Will negates (object); **Spell Resistance** no and yes (object)

You instantly transfer yourself from your current location to any other spot within range. You always arrive at exactly the spot desired---whether by simply visualizing the area or by stating direction. After using this spell, you can't take any other actions until your next turn. You can bring along objects as long as their weight doesn't exceed your maximum load. You may also bring one additional willing Medium or smaller creature (carrying gear or objects up to its maximum load) or its equivalent per three caster levels. A Large creature counts as two Medium creatures, a Huge creature counts as two Large creatures, and so forth. All creatures to be transported must be in contact with one another, and at least one of those creatures must be in contact with you.

If you arrive in a place that is already occupied by a solid body, you and each creature traveling with you take 1d6 points of damage and are shunted to a random open space on a suitable surface within 100 feet of the intended location.

If there is no free space within 100 feet, you and each creature traveling with you take an additional 2d6 points of damage and are shunted to a free space within 1,000 feet. If there is no free space within 1,000 feet, you and each creature travelling with you take an additional 4d6 points of damage and the spell simply fails.

---

</details>

### :white_circle: [Emergency Force Sphere](https://aonprd.com/SpellDisplay.aspx?ItemName=Emergency%20Force%20Sphere)

<details class="card border-primary mb-3"><summary class="card-header">Create a quick hemispherical wall of force to protect you from falling debris.</summary>

**Source** [*Cheliax, Empire of Devils pg. 23*](http://paizo.com/store/downloads/pathfinder/pathfinderCompanion/pathfinderRPG/v5748btpy89ca)
**School** [evocation](https://aonprd.com/SpellDefinitions.aspx?ID=5) [[force](https://aonprd.com/SpellDefinitions.aspx?ID=40)]; **Level** arcanist 4, sorcerer 4, wizard 4
**Casting Time** 1 immediate action
**Components** V
**Range** 5 ft.
**Effect** 5-ft.-radius hemisphere of force centered on you
**Duration** 1 round/level (D)
**Saving Throw** none; **Spell Resistance** no

As *wall of force*, except you create a hemispherical dome of force with hardness 20 and a number of hit points equal to 10 per caster level. The bottom edge of the dome forms a relatively watertight space if you are standing on a reasonably flat surface. The dome shape means that falling debris (such as rocks from a collapsing ceiling) tend to tumble to the side and pile up around the base of the dome. If you make a DC 20 Craft (stonemasonry), Knowledge (engineering), or Profession (architect or engineer) check, the debris is stable enough that it retains its dome-like configuration when the spell ends, otherwise it collapses. Normally this spell is used to buy time for dealing with avalanches, floods, and rockslides, though it is also handy in dealing with ambushes.

---

</details>

### :white_circle: [Dimensional Anchor](https://aonprd.com/SpellDisplay.aspx?ItemName=Dimensional%20Anchor)

<details class="card border-primary mb-3"><summary class="card-header">Bars extradimensional movement.</summary>

**Source** [*PRPG Core Rulebook pg. 270*](http://paizo.com/pathfinderRPG/v5748btpy88yj)\
**School** [abjuration](https://aonprd.com/SpellDefinitions.aspx?ID=1); **Level** arcanist 4, cleric 4, inquisitor 3, medium 3, occultist 4, oracle 4, psychic 4, sorcerer 4, spiritualist 4, summoner 3, summoner (unchained) 4, warpriest 4, wizard 4
**Casting Time** 1 standard action\
**Components** V, S
**Range** medium (100 ft. + 10 ft./level)\
**Effect** ray\
**Duration** 1 min./level\
**Saving Throw** none; **Spell Resistance** yes (object)

A green ray springs from your hand. You must make a ranged touch attack to hit the target. Any creature or object struck by the ray is covered with a shimmering emerald field that completely blocks extradimensional travel. Forms of movement barred by a *dimensional anchor* include *astral projection*, *blink*, *dimension door*, *ethereal jaunt*, *etherealness*, *gate*, *maze*, *plane shift*, *shadow walk*, *teleport*, and similar spell-like abilities. The spell also prevents the use of a *gate* or *teleportation circle* for the duration of the spell.

A *dimensional anchor* does not interfere with the movement of creatures already in ethereal or astral form when the spell is cast, nor does it block extradimensional perception or attack forms. Also, *dimensional anchor* does not prevent summoned creatures from disappearing at the end of a summoning spell.

---

</details>

### :white_circle: [Black Tentacles](https://aonprd.com/SpellDisplay.aspx?ItemName=Black%20Tentacles)

<details class="card border-primary mb-3"><summary class="card-header">Tentacles grapple all creatures within a 20-ft. spread.</summary>

**Source** [*PRPG Core Rulebook pg. 248*](http://paizo.com/pathfinderRPG/v5748btpy88yj)\
**School** [conjuration](https://aonprd.com/SpellDefinitions.aspx?ID=2) ([creation](https://aonprd.com/SpellDefinitions.aspx?ID=13)); **Level** arcanist 4, bloodrager 4, magus 4, psychic 4, sorcerer 4, spiritualist 4, summoner 3, summoner (unchained) 4, witch 4, wizard 4
**Casting Time** 1 standard action\
**Components** V, S, M (octopus or squid tentacle)
**Range** medium (100 ft. + 10 ft./level)\
**Area** 20-ft.-radius spread\
**Duration** 1 round/level (D)\
**Saving Throw** none; **Spell Resistance** no

This spell causes a field of rubbery black tentacles to appear, burrowing up from the floor and reaching for any creature in the area.

Every creature within the area of the spell is the target of a combat maneuver check made to grapple each round at the beginning of your turn, including the round that *black tentacles* is cast. Creatures that enter the area of effect are also automatically attacked. The tentacles do not provoke attacks of opportunity. When determining the tentacles' CMB, the tentacles use your caster level as their base attack bonus and receive a +4 bonus due to their Strength and a +1 size bonus. Roll only once for the entire spell effect each round and apply the result to all creatures in the area of effect.

If the tentacles succeed in grappling a foe, that foe takes 1d6+4 points of damage and gains the grappled condition. Grappled opponents cannot move without first breaking the grapple. All other movement is prohibited unless the creature breaks the grapple first. The *black tentacles* spell receives a +5 bonus on grapple checks made against opponents it is already grappling, but cannot move foes or pin foes. Each round that *black tentacles* succeeds on a grapple check, it deals an additional 1d6+4 points of damage. The CMD of *black tentacles*, for the purposes of escaping the grapple, is equal to 10 + its CMB.

The tentacles created by this spell cannot be damaged, but they can be dispelled as normal. The entire area of effect is considered difficult terrain while the tentacles last.

---

</details>

### :white_circle: [Telekinetic Charge](https://aonprd.com/SpellDisplay.aspx?ItemName=Telekinetic%20Charge)

<details class="card border-primary mb-3"><summary class="card-header">Launches an ally through the air.</summary>

**Source** [*Ultimate Combat pg. 247*](http://paizo.com/pathfinderRPG/v5748btpy8mcz)\
**School** [evocation](https://aonprd.com/SpellDefinitions.aspx?ID=5) [[force](https://aonprd.com/SpellDefinitions.aspx?ID=40)]; **Level** arcanist 4, bloodrager 4, psychic 4, sorcerer 4, spiritualist 4, wizard 4
**Casting Time** 1 standard action\
**Components** V, S
**Range** close (25 ft. + 5 ft./2 levels)\
**Target** one willing creature\
**Duration** instantaneous\
**Saving Throw** Will negates (harmless); **Spell Resistance** yes (harmless)

You telekinetically launch an ally across the battlefield to anywhere within this spell's range. While moving, your ally is flying just above the ground unless you wish otherwise. Movement from this spell provokes attacks of opportunity as normal, although you can lift your ally over objects or out of enemy reach, as long as your ally remains within this spell's range. If your ally lands adjacent to an opponent, he can spend an immediate action to make a melee attack against that opponent with a +2 bonus on the attack roll.

---

</details>

</details>

---

## 5th level :black_circle: :white_circle: :white_circle:

<details class="card bg-light mb-3"><summary class="card-header">Prepared</summary>

### :black_circle: [Monstrous Physique III](https://aonprd.com/SpellDisplay.aspx?ItemName=Monstrous%20Physique%20III)

<details class="card border-primary mb-3"><summary class="card-header">Take the form and some of the powers of a Diminutive or Huge monstrous humanoid.</summary>

**Source** [*Ultimate Magic pg. 229*](http://paizo.com/pathfinderRPG/v5748btpy8k8r)\
**School** [transmutation](https://aonprd.com/SpellDefinitions.aspx?ID=8) ([polymorph](https://aonprd.com/SpellDefinitions.aspx?ID=20)); **Level** alchemist 5, arcanist 5, investigator 5, magus 5, sorcerer 5, wizard 5
**Casting Time** 1 standard action\
**Components** V, S, M (a piece of the creature whose form you plan to assume)
**Range** personal\
**Target** you\
**Duration** 1 minute/level (D)

This spell functions as *monstrous physique II*, except it also allows you to assume the form of a Diminutive or Huge creature of the monstrous humanoid type. If the form you assume has any of the following abilities, you gain the listed ability: burrow 30 feet, climb 90 feet, fly 90 feet (good maneuverability), swim 90 feet, all-around vision, blindsense 30 feet, darkvision 60 feet, low-light vision, scent, blood frenzy, cold vigor, constrict, ferocity, freeze, grab, horrific appearance, jet, leap attack, mimicry, natural cunning, overwhelming, poison, pounce, rake, sound mimicry, speak with sharks, trample, trip, and web. If the creature has the undersized weapons special quality, you gain that quality.

*Diminutive monstrous humanoid*: If the form you take is that of a Diminutive monstrous humanoid, you gain a +6 size bonus to your Dexterity, a --4 penalty to your Strength, and a +1 natural armor bonus.

*Huge monstrous humanoid*: If the form you take is that of a Huge monstrous humanoid, you gain a +6 size bonus to your Strength, a --4 penalty to your Dexterity, and a +6 natural armor bonus.

Mythic Monstrous Physique III

**Source** [*Mythic Adventures pg. 102*](http://paizo.com/products/btpy8ywe?Pathfinder-Roleplaying-Game-Mythic-Adventures)\
Each *mythic monstrous physique* spell must be learned individually, and you must know the respective non-mythic *monstrous physique* spell to learn its mythic version. You don't have to learn them in order, and aren't required to know a lower-level *mythic monstrous physique* spell before you learn a higher-level one (for example, you can learn *mythic monstrous physique II* if you know *monstrous physique II*, even if you don't know *mythic monstrous physique I*). Each *mythic monstrous physique* spell adds the following benefits to its respective non-mythic version.

The spell's bonuses to ability scores increase by 2 each, the natural armor bonus increases by 1, and the ability score penalties decrease by 2 each (minimum penalty of 0). Alternatively, you can cast this spell on another willing creature, changing the range to touch and the target to one creature.

**Augmented (4th)**: If you expend two uses of mythic power, the ability score bonuses increase by an additional 2. Additionally, you can cast this spell on other willing creatures, changing the range to touch and the target to one creature per tier.

---

</details>

### :white_circle: [Telekinesis](https://aonprd.com/SpellDisplay.aspx?ItemName=Telekinesis)

<details class="card border-primary mb-3"><summary class="card-header">Moves object, attacks creature, or hurls object or creature.</summary>

**Source** [*PRPG Core Rulebook pg. 357*](http://paizo.com/pathfinderRPG/v5748btpy88yj)\
**School** [transmutation](https://aonprd.com/SpellDefinitions.aspx?ID=8); **Level** arcanist 5, magus 5, occultist 5, psychic 4, sorcerer 5, spiritualist 5, wizard 5
**Casting Time** 1 standard action\
**Components** V, S
**Range** long (400 ft. + 40 ft./level)\
**Target or Targets** see text\
**Duration** concentration (up to 1 round/level) or instantaneous; see text\
**Saving Throw** Will negates (object) or none; see text; **Spell Resistance** yes (object); see text

You move objects or creatures by concentrating on them. Depending on the version selected, the spell can provide a gentle, sustained force, perform a variety of combat maneuvers, or exert a single short, violent thrust.

*Sustained Force*: A sustained force moves an object weighing no more than 25 pounds per caster level (maximum 375 pounds at 15th level) up to 20 feet per round. A creature can negate the effect on an object it possesses with a successful Will save or with spell resistance.

This version of the spell can last 1 round per caster level, but it ends if you cease concentration. The weight can be moved vertically, horizontally, or in both directions. An object cannot be moved beyond your range. The spell ends if the object is forced beyond the range. If you cease concentration for any reason, the object falls or stops.

An object can be telekinetically manipulated as if with one hand. For example, a lever or rope can be pulled, a key can be turned, an object rotated, and so on, if the force required is within the weight limitation. You might even be able to untie simple knots, though delicate activities such as these require DC 15 Intelligence checks.

*Combat Maneuver*: Alternatively, once per round, you can use *telekinesis* to perform a bull rush, disarm, grapple (including pin), or trip. Resolve these attempts as normal, except that they don't provoke attacks of opportunity, you use your caster level in place of your Combat Maneuver Bonus, and you add your Intelligence modifier (if a wizard) or Charisma modifier (if a sorcerer) in place of your Strength or Dexterity modifier. No save is allowed against these attempts, but spell resistance applies normally. This version of the spell can last 1 round per caster level, but it ends if you cease concentration.

*Violent Thrust*: Alternatively, the spell energy can be spent in a single round. You can hurl one object or creature per caster level (maximum 15) that are within range and all within 10 feet of each other toward any target within 10 feet per level of all the objects. You can hurl up to a total weight of 25 pounds per caster level (maximum 375 pounds at 15th level).

You must succeed on attack rolls (one per creature or object thrown) to hit the target with the items, using your base attack bonus + your Intelligence modifier (if a wizard) or Charisma modifier (if a sorcerer). Weapons cause standard damage (with no Strength bonus; note that arrows or bolts deal damage as daggers of their size when used in this manner). Other objects cause damage ranging from 1 point per 25 pounds (for less dangerous objects) to 1d6 points of damage per 25 pounds (for hard, dense objects). Objects and creatures that miss their target land in a square adjacent to the target.

Creatures who fall within the weight capacity of the spell can be hurled, but they are allowed Will saves (and spell resistance) to negate the effect, as are those whose held possessions are targeted by the spell.

If a telekinesed creature is hurled against a solid surface, it takes damage as if it had fallen 10 feet (1d6 points).

---

</details>

### :white_circle: [Summon Monster V](https://aonprd.com/SpellDisplay.aspx?ItemName=Summon%20Monster%205)

<details class="card border-primary mb-3"><summary class="card-header">Summons extraplanar creature to fight for you.</summary>

**Source** [*PRPG Core Rulebook pg. 352*](http://paizo.com/pathfinderRPG/v5748btpy88yj)\
**School** [conjuration](https://aonprd.com/SpellDefinitions.aspx?ID=2) ([summoning](https://aonprd.com/SpellDefinitions.aspx?ID=23)) [see text]; **Level** arcanist 5, bard 5, cleric 5, medium 4, oracle 5, psychic 5, skald 5, sorcerer 5, spiritualist 5, summoner 4, summoner (unchained) 4, warpriest 5, witch 5, wizard 5
**Casting Time** 1 round\
**Components** V, S, F/DF (a tiny bag and a small candle)
**Range** close (25 ft. + 5 ft./2 levels)\
**Effect** one summoned creature\
**Duration** 1 round/level (D)\
**Saving Throw** none; **Spell Resistance** no

This spell functions like *summon monster I*, except that you can summon one creature from the 5th-level list, 1d3 creatures of the same kind from the 4th-level list, or 1d4+1 creatures of the same kind from a lower-level list.

---

</details>

</details>

---