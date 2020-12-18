% Career prediction program to predict careers based on aptitude and interests
predict(Type) :- 
	interested(Type), fail.

predict(_) :- 
	interest_list(List), write('Your predicted professions (ranked from lower to higher) can be '),
	prediction_list(Pred), write(Pred), nl,
	write('Since the list of your interests is '), write(List), nl.

% Interested rules

interested(Type) :-
	nonvar(Type), assert(asked(Type)), 
	is_linked(Sub, Type), subcheck(Sub).

interested(Type) :-
	var(Type), interest(Type), write('Are you interested in '), write(Type), write(': '),
	read(Reply), Reply = y, assert(asked(Type)), assert(interests(Type)), interested(Type).

subcheck(Sub) :-
	write('Are you interested in '), write(Sub), write(': '),
	read(Reply), Reply = y, assert(interests(Sub)), 
	profession(Prof, Sub), assert(advised(Prof)).

is_linked(X, Y) :- linked(X, Y).
is_linked(X, Y) :- linked(X, Z), linked(Z, Y).

interest_list([Px|Tail]):- retract(interests(Px)), interest_list(Tail).
interest_list([]).

prediction_list([Px|Tail]):- retract(advised(Px)), prediction_list(Tail).
prediction_list([]).

% Facts
profession(software_developer, open_source).
profession(ai_scientist, machine_learning).
profession(astronaut, space).
profession(doctor, biology).
profession(data_analyst, stats).
profession(architect, design).
profession(professor, academics).
profession(lawyer, law).
profession(musician, music).
profession(artist, design).
profession(sports_person, sports).
profession(chartered_accountant, accounts).
profession(army, sports).
profession(navy, sports).
profession(astrophysics, space).
profession(air_force, sports).
profession(banker, finance).
profession(financial_analyst, finance).
profession(civil_servant, history).
profession(psychologist, psychology).
profession(psychiatrist, psychology).
profession(ux_designer, design).
profession(painter, design).
profession(economist, economics).

linked(open_source, computers).
linked(music, arts).
linked(economics, commerce).
linked(computers, science).
linked(psychology, arts).
linked(machine_learning, computers).
linked(biology, science).
linked(space, science).
linked(stats, math).
linked(design, arts).
linked(design, science).
linked(law, arts).
linked(accounts, commerce).
linked(finance, commerce).
linked(accounts, math).
linked(history, arts). 
linked(sports, arts).
linked(academics, science).
linked(academics, commerce).
linked(academics, arts).

interest(commerce).
interest(science).
interest(arts).