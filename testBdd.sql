DROP TABLE IF EXISTS trouver,donner,voitures;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE `trouver` (
  `id` bigint(64) UNSIGNED NOT NULL,
  `lat_dep` double NOT NULL,
  `lng_dep` double NOT NULL,
  `adresse_dep` varchar(255) NOT NULL,
  `lat_arr` double NOT NULL,
  `lng_arr` double NOT NULL,
  `adresse_arr` varchar(255) NOT NULL,
  `date_heur` datetime NOT NULL,
  `id_user` bigint(64) UNSIGNED NOT NULL,
  `etat` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `trouver` (`id`, `lat_dep`, `lng_dep`, `adresse_dep`, `lat_arr`, `lng_arr`, `adresse_arr`, `date_heur`, `id_user`, `etat`) VALUES


(1, 48.877505, 2.343289, '28 Rue de Maubeuge, 75009 Paris', 48.869240, 2.345665, '17 Rue des Jeuneurs, 75002 Paris', '2019-12-07 13:57:12', 2, 1),
(2, 48.848067, 2.301280, 'Boulevard de Grenelle, 75015 Paris', 48.871928, 2.348330, '46 Rue de l\'Échiquier, 75010 Paris', '2019-12-08 08:38:41', 3, 2),
(3, 48.837187, 2.322750, '94 Avenue du Maine, 75014 Paris', 48.866348, 2.334195, '24 Avenue de l\'Opéra, 75001 Paris', '2019-12-09 16:19:09', 4, 1),
(4, 48.829307, 2.306654, 'Rue Vercingétorix, 75014 Paris', 48.844017, 2.382108, '133 Avenue Daumesnil, 75012 Paris', '2019-12-10 22:40:28', 5, 2),
(5, 48.850477, 2.353275, 'Quai de la Tournelle, 75005 Paris', 48.836328, 2.326721, '47 Rue Froidevaux, 75014 Paris', '2019-12-11 05:56:35', 6, 1),
(6, 48.874971, 2.305789, '177 Boulevard Haussmann, 75008 Paris', 48.857998, 2.300115, '52 Avenue Rapp, 75007 Paris', '2019-12-12 09:09:09', 7, 2),
(7, 48.851543, 2.390617, '242 Boulevard Voltaire, 75011 Paris', 48.858122, 2.381906, '119 Rue de la Roquette, 75011 Paris', '2019-12-13 22:29:31', 106, 1),
(8, 48.829112, 2.343169, '104 Rue de la Glacière, 75013 Paris', 48.839173, 2.359177, '5 Boulevard Saint-Marcel, 75005 Paris', '2019-12-14 14:29:31', 107, 1),
(9, 48.836630, 2.324300, '13 Rue Cels, 75014 Paris', 48.830906, 2.312426, '151 Rue Raymond Losserand, 75014 Paris', '2019-12-15 09:29:31', 108, 1),
(10, 48.851466, 2.274150, '3 Rue Agar, 75016 Paris', 48.849368, 2.292184, '3 Rue Fallempin, 75015 Paris', '2019-12-16 20:29:31', 109, 1),
(11, 48.886572, 2.325435, '8 Rue Hélène, 75018 Paris', 48.882328, 2.304256, '51 Rue de Prony, 75017 Paris', '2019-12-17 12:29:31', 110, 1);






CREATE TABLE `donner` (
  `id` bigint(64) UNSIGNED NOT NULL,
  `lat` double NOT NULL,
  `lng` double NOT NULL,
  `adresse` varchar(255) NOT NULL,
  `date_heur` datetime NOT NULL,
  `heur_liberer` datetime NOT NULL,
  `id_user` bigint(64) UNSIGNED NOT NULL,
  `etat` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `donner` (`id`, `lat`, `lng`, `adresse`, `date_heur`, `heur_liberer`, `id_user`, `etat`) VALUES

(1, 48.869240, 2.345665, '17 Rue des Jeuneurs, 75002 Paris', '2019-12-08 10:55:12', '2019-12-08 10:55:12', 2, 1),
(2, 48.871928, 2.348330, '46 Rue de l\'Échiquier, 75010 Paris', '2019-12-09 18:38:41', '2019-12-09 18:38:41', 3, 2),
(3, 48.866348, 2.334195, '24 Avenue de l\'Opéra, 75001 Paris', '2019-12-10 06:19:09', '2019-12-10 06:19:09', 4, 1),
(4, 48.844017, 2.382108, '133 Avenue Daumesnil, 75012 Paris', '2019-12-11 09:40:28', '2019-12-11 09:40:28', 5, 2),
(5, 48.836328, 2.326721, '47 Rue Froidevaux, 75014 Paris', '2019-12-12 15:30:35', '2019-12-12 15:30:35', 6, 1),
(6, 48.857998, 2.300115, '52 Avenue Rapp, 75007 Paris', '2019-12-13 12:12:12', '2019-12-13 12:12:12', 7, 2),
(7, 48.858122, 2.381906, '119 Rue de la Roquette, 75011 Paris', '2019-12-14 05:29:31', '2019-12-19 05:29:31', 101, 1),
(8, 48.839173, 2.359177, '5 Boulevard Saint-Marcel, 75005 Paris', '2019-12-15 06:30:31', '2019-12-20 06:30:31', 102, 1),
(9, 48.830906, 2.312426, '151 Rue Raymond Losserand, 75014 Paris', '2019-12-16 07:40:31', '2019-12-21 07:40:31', 103, 1),
(10, 48.849368, 2.292184, '3 Rue Fallempin, 75015 Paris', '2019-12-17 08:25:31', '2019-12-22 08:25:31', 104, 1),
(11, 48.882328, 2.304256, '51 Rue de Prony, 75017 Paris', '2019-12-18 09:55:31', '2019-12-23 09:55:31', 105, 1);






CREATE TABLE `voitures` (
  `id` bigint(64) UNSIGNED NOT NULL,
  `marque` varchar(50) NOT NULL,
  `modele` varchar(50) NOT NULL,
  `couleur` varchar(60) NOT NULL,
  `matricule` varchar(50) NOT NULL,
  `type` varchar(30) NOT NULL,
  `annee` varchar(4) NOT NULL,
  `id_user` bigint(64) UNSIGNED NOT NULL,
  `selected` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `voitures` (`id`, `marque`, `modele`, `couleur`, `matricule`, `type`, `annee`, `id_user`, `selected`) VALUES
(1, 'Seat', 'Ibiza', 'Gris', 'ON-357-LA', 'Citadine', '', 101, 1),
(2, 'Citroen', 'C3', 'Blanc', 'BW-845-KF', 'Citadine', '', 102, 1),
(3, 'Peugeot', '407', 'Noir', 'WS-768-RZ', 'Berline et 4x4', '', 103, 1),
(4, 'Renault', 'clio', 'Indigo', 'FF-877-JK', 'Citadine', '',104, 1),
(5, 'Mercedes-Benz', 'Classe C', 'Orange foncé', 'GU-912-CD', 'Berline et 4x4', '', 105, 1),
(6, 'Volkswagen', 'golf 7', 'Gris', 'NS-154-AH', 'Berline et 4x4', '', 106, 1),
(7, 'Toyota', 'GT86', 'Rouge', 'TY-860-AT', 'Coupé', '', 107, 1),
(8, 'Opel', 'Corsa', 'Rouge', 'GG-CG-980', 'Citadine', '', 108, 1),
(9, 'Seat', 'Leon', 'Vert', 'GG-AO-410', 'Citadine', '', 109, 1),
(10, 'Citroen', 'C4', 'Jaune', 'EP-526-ME', 'Citadine', '', 110, 1),
(11, 'Peugeot', '206', 'GRIS', 'BA-100-PD', 'Citadine', '', 103, 1);


ALTER TABLE `trouver`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `voitures`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `donner`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `donner`
  MODIFY `id` bigint(64) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13813;

ALTER TABLE `trouver`
  MODIFY `id` bigint(64) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3428;

ALTER TABLE `voitures`
  MODIFY `id` bigint(64) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7507;
COMMIT;
