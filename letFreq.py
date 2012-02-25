# think DSU

def most_frequent(s):
  let_dict={}
  for let in s:
    let_lower = let.lower()
    if let_lower in let_dict: 
      let_dict[let_lower] += 1
    else: # let not yet in dictionary
      let_dict[let_lower] = 1
  print let_dict    
   
  # at this point we have an unsorted dictionary with letters and their frequencies
  letList = []
  for letter in let_dict:
    letList.append((let_dict[letter], letter))
  letList.sort(reverse=True)
  
  for letter in range(len(letList)):
    print letter, letList[letter][1], letList[letter][0]

  
test_string = "\
The warning by the deputy head of its armed forces, quoted by a semi-official news agency, came as Tehran also appeared to place limits on a visit by a team of United Nations nuclear officials, saying the investigators would not go to nuclear facilities, despite earlier reports that its members had sought permission to inspect a military complex outside Tehran.\
\
Without mentioning Israel directly, Mohammed Hejazi, the deputy armed forces head, said on Tuesday: Our strategy now is that if we feel our enemies want to endanger Iran’s national interests, and want to decide to do that, we will act without waiting for their actions,Reuters reported. Divisions in Iran’s leadership make it difficult to interpret the government’s intentions, but the statement showed a new level of aggressiveness in Iran’s rhetoric.\
The statement came a day after a team from the International Atomic Energy Agency arrived in Tehran on Monday for the second time in three weeks. The Associated Press quoted the Foreign Ministry spokesman, Ramin Mehmanparast, as saying the investigators from the International Atomic Energy Agency had no plans to visit the contentious nuclear sites, which the West maintains are part of a covert weapons program.\
\
The inspectors did ask on Monday to see a military complex outside Tehran that is a suspected secret weapons-making location, Iranian radio said, according to The A.P. It was not clear whether the Iranian authorities had specifically turned down the reported request. I.A.E.A. officials did not immediately return calls seeking clarification.\
\
    As the I.A.E.A. delegation left its headquarters in Vienna late Sunday, its leader, Herman Nackaerts, said the delegation wished to investigate the possible military dimensions that Tehran insists the program does not have and that the inspectors’ previous visit did nothing to resolve.\
\
    International tension has been rising steadily, as Iran claims significant technological advances in uranium enrichment and threatens retaliation against countries that pursue sanctions against it, including a boycott of its oil.\
\
    Shortly after the I.A.E.A. team arrived for talks with Iranian officials, the Iranian government signaled that it might expand a ban on oil shipments to Britain and France, announced on Sunday, to cover other European powers that it deems “hostile” because of broader economic sanctions by the European Union that are scheduled to come into force on July 1. The ban was apparently announced to pre-empt those sanctions, which include a boycott on new purchases.\
\
    Iran’s deputy oil minister, Ahmad Qalebani, said that oil exports to Germany, Greece, Italy the Netherlands, Portugal and Spain might also be banned, state media reported.\
\
    Undoubtedly, if the hostile actions of certain European countries continue, oil exports to these countries will be stopped, Mr. Qalebani, who is also the managing director of the National Iranian Oil Company, was quoted as saying by the Mehr News Agency.\
\
    The threat reflected speculation that Iran may be trying to sow division in the 27-nation European Union between the members that do not rely heavily on Iranian oil and those that do.\
\
    Over all, the European Union buys about 18 percent of the oil that Iran exports. But those exports are much more important to Italy and Spain, which each get about one-eighth of their oil supplies from Iran, or to Greece, which gets one-third, than they are to Britain and Germany, which get only 1 percent of their oil from Iran, or to France, which gets only 3 percent.\
\
    Despite Mr. Qalebani’s remarks, Iran may hesitate to compound the economic harm it suffers from existing sanctions by forfeiting significant revenue from oil sales to Europe now. Even so, the standoff between Iran and the West sometimes resembles a poker game with potentially lethal stakes, as both Iran and its adversaries maneuver for advantage with no way of knowing their opponent’s ultimate intentions.\
\
    British leaders, for instance, are trying to dissuade Israel from contemplating a military strike at Iran’s nuclear facilities, while President Mahmoud Ahmadinejad of Iran boasts of enhanced enrichment capabilities.\
\
    Over the weekend, William Hague, the British foreign secretary, said that while the West should leave all of its options open, a military strike would have “enormous downsides,” and that Britain’s main priority was to “bring Iran back to the table” through diplomacy and economic pressure.\
\
    Iran, for its part, announced new military exercises on Monday “in a bid to prevent such aggressions” by Israel and the West, the semiofficial Fars News Agency reported. “The grandeur and mightiness of the country’s armed forces is a deterrent element against enemies’ recent aggressions and threats,” said Maj. Gen. Mohammad Ali Jafari, the commander in chief of the Islamic Revolutionary Guards Corps.\
\
    The leader of the delegation of inspectors, Mr. Nackaerts, said “We hope to have some concrete results after this trip.” Though weapons development was the most important question, he said, “We want to tackle all outstanding issues.”\
\
    Mr. Nackaerts, the atomic agency’s deputy director general, warned that “this is of course a complex issue, which may take a while,” according to a transcript of his remarks made available on Monday by agency officials.\
\
    The latest visit is scheduled to last two days, though it may be extended, as the last one was. Diplomats who were briefed on the discussions held on the last visit said that Iranian officials failed to address the major concerns about Iran’s activities that were raised in a report issued by the agency in November.\
\
    Some of the latest Western worries center on a new uranium enrichment plant at Fordo, Iran, which is buried deep underground, making it much harder to monitor or, presumably, to attack.\
\
    Iran tried to keep construction of the plant secret, but Western intelligence agencies confirmed its existence in 2009; Iran then insisted that it had intended to make the plant publicly known all along.\
\
    Western officials appear to be divided over whether Iran is shifting toward a more conciliatory posture or is playing for time to pursue its uranium enrichment program, which it says is for strictly peaceful purposes.\
\
    Last week, in a letter to the European Union, Iran called for new talks “at the earliest possibility” with the group of six powers that have negotiated with Iran in the past on the nuclear issue: Britain, China, France, Germany, Russia and the United States.\
\
    In the past, calls for talks from Iran have often been accompanied by warlike statements that it is honing its military capabilities. Iran’s defense minister, Brig. Gen. Ahmad Vahidi, said Monday that the country had begun several projects to build new advanced warplanes, according to Press TV, a state-financed satellite broadcaster.\
\
    On its Web site, the broadcaster showed a photograph of what it said was a long-range land-to-sea missile called Qader, or Capable, being fired during war games in southern Iran."
test_string = test_string.strip()
test_string = test_string.split()
letters = "".join(test_string)
most_frequent(letters)
    