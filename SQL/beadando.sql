  USE  Fjanos;
  
show databases;

DROP TABLE Felhasznalo;

create table Felhasznalo
(
	Felhasznalonev varchar(20) not null,
    Email varchar(40) not null,
    MeghivoSz varchar(20),
    Kor integer not null,
    Jelszo varchar(20) not null,
    constraint pk_felhasznalo primary key(Felhasznalonev),
    constraint Fk_Meghivoszemely foreign key(Meghivosz) references Felhasznalo(Felhasznalonev)
    
);

INSERT INTO Felhasznalo(Felhasznalonev,Email,Meghivosz,Kor,Jelszo) VALUES ('Piszkos Fred', 'kapitany@rejto.com', null, 62, '12345');
INSERT INTO Felhasznalo(Felhasznalonev,Email,Meghivosz,Kor,Jelszo) VALUES ('Tuskó Hopkins', 'tusko_h@rejto.com', null, 43, '12345');
INSERT INTO Felhasznalo(Felhasznalonev,Email,Meghivosz,Kor,Jelszo) VALUES ('Gorcsev Iván', 'gorcsev@rejto.com', null, 48, '12345');
INSERT INTO Felhasznalo(Felhasznalonev,Email,Meghivosz,Kor,Jelszo) VALUES ('Szokoloff', 'szokoloff@rejto.com', null, 41, '12345');
INSERT INTO Felhasznalo(Felhasznalonev,Email,Meghivosz,Kor,Jelszo) VALUES ('Fülig Jimmy', 'fulig@rejto.com', 'Piszkos Fred', 32, '12345');
INSERT INTO Felhasznalo(Felhasznalonev,Email,Meghivosz,Kor,Jelszo) VALUES ('Senki Alfonz', 'senki@rejto.com', 'Tuskó Hopkins', 28, '12345');
INSERT INTO Felhasznalo(Felhasznalonev,Email,Meghivosz,Kor,Jelszo) VALUES ('Török Szultán', 'szultan@rejto.com', 'Tuskó Hopkins', 55, '12345');
INSERT INTO Felhasznalo(Felhasznalonev,Email,Meghivosz,Kor,Jelszo) VALUES ('A Nagy Levin', 'levin@rejto.com', 'Tuskó Hopkins', 54, '12345');
INSERT INTO Felhasznalo(Felhasznalonev,Email,Meghivosz,Kor,Jelszo) VALUES ('Galamb', 'galamb@rejto.com', 'Tuskó Hopkins', 29, '12345');
INSERT INTO Felhasznalo(Felhasznalonev,Email,Meghivosz,Kor,Jelszo) VALUES ('Sirone kapitány', 'sirone@rejto.com', null, 29, '12345');
INSERT INTO Felhasznalo(Felhasznalonev,Email,Meghivosz,Kor,Jelszo) VALUES ('Henry Fécamp', 'Henry_F@rejto.com', 'Sirone kapitány', 71, '12345');
INSERT INTO Felhasznalo(Felhasznalonev,Email,Meghivosz,Kor,Jelszo) VALUES ('Ligert írnok ', 'ligert@rejto.com', 'Fülig Jimmy', 61, '12345');
INSERT INTO Felhasznalo(Felhasznalonev,Email,Meghivosz,Kor,Jelszo) VALUES ('Rozsdás', 'rozsdas@rejto.com', 'Piszkos Fred', 61, '12345');
INSERT INTO Felhasznalo(Felhasznalonev,Email,Meghivosz,Kor,Jelszo) VALUES ('Bradford százados', 'ford@rejto.com', 'Piszkos Fred', 55, '12345');
INSERT INTO Felhasznalo(Felhasznalonev,Email,Meghivosz,Kor,Jelszo) VALUES ('Thomas Leven', 'leven@rejto.com', 'Piszkos Fred', 55, '12345');
INSERT INTO Felhasznalo(Felhasznalonev,Email,Meghivosz,Kor,Jelszo) VALUES ('Kvang generális', 'kvang@rejto.com', 'Thomas Leven', 55, '12345');
INSERT INTO Felhasznalo(Felhasznalonev,Email,Meghivosz,Kor,Jelszo) VALUES ('Morrison Snyder', 'Morrison@rejto.com', 'Kvang generális', 15, '12345');
INSERT INTO Felhasznalo(Felhasznalonev,Email,Meghivosz,Kor,Jelszo) VALUES ('Kalóz Pepi', 'pepi@rejto.com', 'Kvang generális', 75, '12345');
INSERT INTO Felhasznalo(Felhasznalonev,Email,Meghivosz,Kor,Jelszo) VALUES ('Vörös Vaszics', 'vaszics@rejto.com', 'Piszkos Fred', 19, '12345');
INSERT INTO Felhasznalo(Felhasznalonev,Email,Meghivosz,Kor,Jelszo) VALUES ('Buzgó Mócsing', 'buzgo@rejto.com', null, 21, '12345');

CREATE TABlE Bejegyzesek 
(
	BFelhasznalonev varchar(50) not null,
    Letrehozas_datuma date,
    Utolso_modositas_datuma date,
    Content varchar(555),
    ValaszID integer,
    Likok_szama integer,
    id integer auto_increment,
    constraint Pr_id primary key(id),
    Constraint Fk_Bfelhasznalo foreign key(BFelhasznalonev)references Felhasznalo(Felhasznalonev),
    Constraint Fk_ValaszID foreign key(ValaszID)references Bejegyzesek(id)
);
INSERT INTO Bejegyzesek(BFelhasznalonev,Letrehozas_datuma,Utolso_modositas_datuma,Content,ValaszID,Likok_szama) VALUES ('Fülig Jimmy', '1931-01-12', '1931-01-12', 'Uram! A késemért jöttem!',1,5);
INSERT INTO Bejegyzesek(BFelhasznalonev,Letrehozas_datuma,Utolso_modositas_datuma,Content,ValaszID,Likok_szama) VALUES ('Fülig Jimmy', '1931-01-13', '1931-01-13', 'A Török Szultán már két napja nem ment ki az utcára, mert valaki ellopta a nadrágját. Ezt a ruhadarabot nehéz nélkülözni, ha valaki sétálni megy.',2,2);
INSERT INTO Bejegyzesek(BFelhasznalonev,Letrehozas_datuma,Utolso_modositas_datuma,Content,ValaszID,Likok_szama) VALUES ('Kvang generális', '1931-01-15', '1931-01-15', 'De te mindig mást gondolsz, amikor mást mondasz.',1,5);
INSERT INTO Bejegyzesek(BFelhasznalonev,Letrehozas_datuma,Utolso_modositas_datuma,Content,ValaszID,Likok_szama) VALUES ('A Nagy Levin', '1931-01-16', '1931-01-16', 'Mi a tanulság?',2,3);
INSERT INTO Bejegyzesek(BFelhasznalonev,Letrehozas_datuma,Utolso_modositas_datuma,Content,ValaszID,Likok_szama) VALUES ('Fülig Jimmy', '1931-01-17', '1931-01-17', 'Nem tudom!',2,5);
INSERT INTO Bejegyzesek(BFelhasznalonev,Letrehozas_datuma,Utolso_modositas_datuma,Content,ValaszID,Likok_szama) VALUES ('Ligert írnok', '1931-01-18', '1931-01-18', 'De egészen bizonyos, hogy az ügy mögött tanulságos következtetések húzódnak meg.',2,5);
INSERT INTO Bejegyzesek(BFelhasznalonev,Letrehozas_datuma,Utolso_modositas_datuma,Content,ValaszID,Likok_szama) VALUES ('Tuskó Hopkins', '1931-01-19', '1931-01-19', 'És most az dobja rám az elsö követ, aki nem fél attól, hogy szájon vágom!',1,5);
INSERT INTO Bejegyzesek(BFelhasznalonev,Letrehozas_datuma,Utolso_modositas_datuma,Content,ValaszID,Likok_szama) VALUES ('Sirone kapitány', '1931-01-20', '1931-01-20', 'Ide hallgass, Fred, és maga is figyeljen ide, Fönök: akarnak fejenként ötezer fontot keresni?',3,5);
INSERT INTO Bejegyzesek(BFelhasznalonev,Letrehozas_datuma,Utolso_modositas_datuma,Content,ValaszID,Likok_szama) VALUES ('Fülig Jimmy', '1931-01-21', '1931-01-21', 'Attól függ, hogyan. Illetve attól se függ.',3,5);
INSERT INTO Bejegyzesek(BFelhasznalonev,Letrehozas_datuma,Utolso_modositas_datuma,Content,ValaszID,Likok_szama) VALUES ('Tuskó Hopkins', '1931-01-20', '1931-01-20', 'Adj egy pohár vöröset, Galamb, de ne tisztán, hígítsd valamivel.',4,2);
INSERT INTO Bejegyzesek(BFelhasznalonev,Letrehozas_datuma,Utolso_modositas_datuma,Content,ValaszID,Likok_szama) VALUES ('Galamb', '1931-01-21', '1931-01-21', 'Két deci vörösbort, három deci rummal hígítva.',4,9);
INSERT INTO Bejegyzesek(BFelhasznalonev,Letrehozas_datuma,Utolso_modositas_datuma,Content,ValaszID,Likok_szama) VALUES ('Buzgó Mócsing', '1931-01-13', '1931-01-13', 'Miért zárták be, Galamb?',5,5);
INSERT INTO Bejegyzesek(BFelhasznalonev,Letrehozas_datuma,Utolso_modositas_datuma,Content,ValaszID,Likok_szama) VALUES ('Galamb', '1931-01-14', '1931-01-14', 'Csendháborítás miatt.Öt évre!',5,5);
INSERT INTO Bejegyzesek(BFelhasznalonev,Letrehozas_datuma,Utolso_modositas_datuma,Content,ValaszID,Likok_szama) VALUES ('Buzgó Mócsing', '1931-01-15', '1931-01-15', 'Az hogy lehet?',5,5);
INSERT INTO Bejegyzesek(BFelhasznalonev,Letrehozas_datuma,Utolso_modositas_datuma,Content,ValaszID,Likok_szama) VALUES ('Galamb', '1931-01-16', '1931-01-16', 'Mikor kimásztam az ablakon, leejtettem egy tükröt, és a csörömpölésre összeszaladtak a lakók.',5,5);
INSERT INTO Bejegyzesek(BFelhasznalonev,Letrehozas_datuma,Utolso_modositas_datuma,Content,ValaszID,Likok_szama) VALUES ('Morrison Snyder', '1931-01-17', '1931-01-17', 'Valaki azt mondja, hogy két cápa úszott már a fiú felé, de amikor meglátták a kapitányt, csüggedten visszafordultak!',6,11);
INSERT INTO Bejegyzesek(BFelhasznalonev,Letrehozas_datuma,Utolso_modositas_datuma,Content,ValaszID,Likok_szama) VALUES ('Henry Fécamp', '1931-01-17', '1931-01-17', 'Grófnö, egy okos embert csak kétszer lehet becsapni! ',7,5);

-- 1. Kik az "ős" felhasználók?
select*from Felhasznalo where Meghivosz is null;

-- 2. Kik nem "ős" felhasználók?
select*from Felhasznalo where Meghivosz is not null;

-- 3. Adjuk meg a felhasználókat koruk szerint rendezve.
select*from Felhasznalo order by kor;
-- 4. Melyik a legtöbbet like-olt bejegyzés?
select*from Bejegyzesek where Likok_szama = (select max(Likok_szama) from Bejegyzesek);

-- 5. Adjuk meg azon Bejegyzéseket, amelyek említik az "adatbázis" szót.

select*from Bejegyzesek where Content like '%adatbázis%';
-- 5.1. Adjuk meg azon Bejegyzéseket, amelyek említik az "Galamb" szót.

select*from Bejegyzesek where Content like '%Galamb%';

-- 6. Adjuk meg azon felhasználókat, akiknek a kora 18 és 21 között van.
SELECT * FROM Felhasznalo WHERE kor BETWEEN 18 AND 21;

-- 7. Melyek azok a bejegyzések ahol a likeok száma meghaladja a 10-et?
SELECT * FROM Bejegyzesek WHERE Likok_szama >= 10;
-- 8. Kik azok a felhasználók akinek van olyan bejegyzése amin több mint 10 like van?

-- 9. Adjuk meg azon felhasználókat, akik meghívtak valakit.
SELECT distinct Meghivosz from Felhasznalo where Meghivosz is not null;
-- 10. Adjuk meg azon felhasználó(kat), akik a legtöbb embert hívták meg.
SELECT distinct max(Meghivosz) from Felhasznalo where Meghivosz is not null;
-- 11. Adjuk meg, hogy a bejegyzésekre hány válasz érkezett.

-- 12. Adjuk meg azokat a felhasználókat akik meghívottjai közt van olyan akinek több mint 2 bejegyzése van.

-- 13. Adjuk meg a legtöbbet likeolt felhasználókat. (Akik bejegyzései a legtöbb likeot kapták)


-- 14. (Extra) Adjuk meg azon felhasználó(kat), akik a legtöbb embert hívták meg. ha számoljuk a meghívott által meghívott személyket és az általuk meghívottakat


SELECT Bejegyzesek.felhasznalo;

	


 
