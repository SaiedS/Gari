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
(2, 48.869240, 2.345665, '17 Rue des Jeuneurs, 75002 Paris', 48.871928, 2.348330, '46 Rue de l\'Échiquier, 75010 Paris', '2019-12-08 08:38:41', 3, 2),
(3, 48.871928, 2.348330, '46 Rue de l\'Échiquier, 75010 Paris', 48.866348, 2.334195, '24 Avenue de l\'Opéra, 75001 Paris', '2019-12-09 16:19:09', 4, 1),
(4, 48.866348, 2.334195, '24 Avenue de l\'Opéra, 75001 Paris', 48.844017, 2.382108, '133 Avenue Daumesnil, 75012 Paris', '2019-12-10 22:40:28', 5, 2),
(5, 48.844017, 2.382108, '133 Avenue Daumesnil, 75012 Paris', 48.836328, 2.326721, '47 Rue Froidevaux, 75014 Paris', '2019-12-11 05:56:35', 6, 1),
(6, 48.836328, 2.326721, '47 Rue Froidevaux, 75014 Paris', 48.857998, 2.300115, '52 Avenue Rapp, 75007 Paris', '2019-12-12 09:09:09', 7, 2);

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
(1, 48.8774604, 2.3436713, '32 Rue de Maubeuge, 75009 Paris, France', '2019-12-18 22:29:31', '2019-12-18 22:29:31', 17, 1),
(2, 48.834516, 2.331960, '10 Place Denfert-Rochereau P', '2019-12-10 03:00:43', '2019-12-10 03:00:43', 2, 2),
(3, 48.84619741239477, 2.3512809164844, '59 Rue du Cardinal Lemoine,Paris, France, 75005','2019-12-18 22:38:30', '2019-12-18 22:38:30', 22, 1),
(4, 48.8774054, 2.3436725, '32 Rue de Maubeuge, 75009 Paris, France', '2019-12-18 22:39:44', '2019-12-18 22:39:44', 17, 1),
(5, 48.8774078, 2.3436731, '32 Rue de Maubeuge, 75009 Paris, France', '2019-12-18 22:40:25', '2019-12-18 22:40:25', 17, 1),
(6, 48.8775908, 2.3434439, '32-34 Rue de Maubeuge, 75009 Paris, France', '2019-12-18 22:54:02', '2019-12-18 22:54:02', 22, 2),
(7, 48.877411, 2.3436763, '32 Rue de Maubeuge, 75009 Paris, France', '2019-12-18 22:54:05', '2019-12-18 22:54:05', 17, 2);

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
(1, 'Seat', 'Ibiza', 'Gris', 'ON-357-LA', 'Citadine', '', 2, 1),
(2, 'Citroen', 'C3', 'Blanc', 'BW-845-KF', 'Citadine', '', 3, 1),
(3, 'Peugeot', '407', 'Noir', 'WS-768-RZ', 'Berline et 4x4', '', 4, 1),
(4, 'Renault', 'clio', 'Indigo', 'FF-877-JK', 'Citadine', '', 5, 1),
(5, 'Mercedes-Benz', 'Classe C', 'Orange foncé', 'GU-912-CD', 'Berline et 4x4', '', 6, 1),
(6, 'Volkswagen', 'golf 7', 'Gris', 'NS-154-AH', 'Berline et 4x4', '', 7, 1),
(7, 'Toyota', 'GT86', 'Rouge', 'TY-860-AT', 'Coupé', '', 8, 1);



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