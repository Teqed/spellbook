import json
with open("spell_full.json", "r") as read_file:
    allspells = json.load(read_file)

# Filter python objects with list comprehensions
wiz_spell_0 = [x for x in allspells if x['wiz'] == '0']
wiz_spell_1 = [x for x in allspells if x['wiz'] == '1']
wiz_spell_2 = [x for x in allspells if x['wiz'] == '2']
wiz_spell_3 = [x for x in allspells if x['wiz'] == '3']
wiz_spell_4 = [x for x in allspells if x['wiz'] == '4']
wiz_spell_5 = [x for x in allspells if x['wiz'] == '5']
wiz_spell_6 = [x for x in allspells if x['wiz'] == '6']
wiz_spell_7 = [x for x in allspells if x['wiz'] == '7']
wiz_spell_8 = [x for x in allspells if x['wiz'] == '8']
wiz_spell_9 = [x for x in allspells if x['wiz'] == '9']

# Transform python object back into json
wiz_spell_0_json = json.dumps(wiz_spell_0)
wiz_spell_1_json = json.dumps(wiz_spell_1)
wiz_spell_2_json = json.dumps(wiz_spell_2)
wiz_spell_3_json = json.dumps(wiz_spell_3)
wiz_spell_4_json = json.dumps(wiz_spell_4)
wiz_spell_5_json = json.dumps(wiz_spell_5)
wiz_spell_6_json = json.dumps(wiz_spell_6)
wiz_spell_7_json = json.dumps(wiz_spell_7)
wiz_spell_8_json = json.dumps(wiz_spell_8)
wiz_spell_9_json = json.dumps(wiz_spell_9)

# Write json to file

f = open("spell0.json", "a")
f.write(wiz_spell_0_json)
f.close()

f = open("spell1.json", "a")
f.write(wiz_spell_1_json)
f.close()

f = open("spell2.json", "a")
f.write(wiz_spell_2_json)
f.close()

f = open("spell3.json", "a")
f.write(wiz_spell_3_json)
f.close()

f = open("spell4.json", "a")
f.write(wiz_spell_4_json)
f.close()

f = open("spell5.json", "a")
f.write(wiz_spell_5_json)
f.close()

f = open("spell6.json", "a")
f.write(wiz_spell_6_json)
f.close()

f = open("spell7.json", "a")
f.write(wiz_spell_7_json)
f.close()

f = open("spell8.json", "a")
f.write(wiz_spell_8_json)
f.close()

f = open("spell9.json", "a")
f.write(wiz_spell_9_json)
f.close()