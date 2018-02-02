--
-- Volcado de datos para la tabla `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'admin');

-- --------------------------------------------------------

--
-- Volcado de datos para la tabla `auth_group_permissions`
--

INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
(4, 1, 19),
(5, 1, 20),
(6, 1, 21),
(7, 1, 22),
(8, 1, 23),
(9, 1, 24),
(10, 1, 25),
(11, 1, 26),
(12, 1, 27),
(13, 1, 28),
(14, 1, 29),
(15, 1, 30),
(16, 1, 31),
(17, 1, 32),
(18, 1, 33),
(19, 1, 34),
(20, 1, 35),
(21, 1, 36),
(22, 1, 37),
(23, 1, 38),
(24, 1, 39),
(25, 1, 40),
(26, 1, 41),
(27, 1, 42);

-- --------------------------------------------------------

-- CREATE TABLE `time_worked_timeworked` (
--   `id` int(11) NOT NULL,
--   `date` date DEFAULT NULL,
--   `start` varchar(80) NOT NULL,
--   `finish` varchar(20) NOT NULL,
--   `context` varchar(120) NOT NULL,
--   `location` varchar(120) NOT NULL,
--   `img` varchar(100) NOT NULL,
--   `hours` int(11) NOT NULL,
--   `minutes` int(11) NOT NULL,
--   `created_at` datetime(6) NOT NULL,
--   `user_id` int(11) NOT NULL,
--   `work_order_id` int(11) NOT NULL
-- ) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --
-- -- Volcado de datos para la tabla `time_worked_timeworked`
-- --

-- INSERT INTO `time_worked_timeworked` (`id`, `date`, `start`, `finish`, `context`, `location`, `img`, `hours`, `minutes`, `created_at`, `user_id`, `work_order_id`) VALUES
-- (1, '2018-01-29', '20:52', '22:52', 'mc', 'mx', 'albums/images/2018/01/13/54edfeee0f266c08c6ce7e8662de65d2.png', 2, 0, '2018-01-13 02:52:30.534483', 1, 1),
-- (2, '2018-01-31', '03:52', '19:45', 'mx', 'mx', 'albums/images/2018/01/31/trabajando_guh4ARL.jpg', 15, 53, '2018-01-13 02:53:19.256029', 1, 1),
-- (3, '2018-01-31', '23:25', '23:55', 'mmm', 'mx', 'albums/images/2018/01/31/cuidar_la_vista_ordenador-1024x683.jpg', 0, 30, '2018-01-13 03:28:44.919768', 1, 1),
-- (4, '2018-01-31', '01:29', '02:29', 'mcmc', 'mx', 'albums/images/2018/01/31/trabajando.jpg', 1, 0, '2018-01-13 03:30:05.561516', 1, 1),
-- (5, '2018-01-08', '19:39', '21:40', 'kmofekmoerkm', 'mx', 'albums/images/2018/01/13/23550950_10212662353168271_5668330830254242575_o.jpg', 2, 1, '2018-01-13 03:40:28.763217', 1, 1),
-- (6, '2018-01-12', '16:04', '17:04', 'descripcion', 'mx', 'albums/images/2018/01/13/23550950_10212662353168271_5668330830254242575_o_b71N1oB.jpg', 1, 0, '2018-01-13 22:04:46.303643', 4, 1),
-- (7, '2018-01-15', '22:06', '22:06', 'description', 'mx', 'albums/images/2018/01/16/54edfeee0f266c08c6ce7e8662de65d2.png', 0, 0, '2018-01-16 04:07:07.968556', 2, 1),
-- (8, '2018-01-15', '19:23', '22:30', 'txt', 'mx', 'albums/images/2018/01/16/54edfeee0f266c08c6ce7e8662de65d2_g1t7orK.png', 3, 7, '2018-01-16 04:24:12.987537', 2, 1),
-- (9, '2018-01-20', '19:59', '22:59', 'context', 'mx', 'albums/images/2018/01/20/23550950_10212662353168271_5668330830254242575_o.jpg', 3, 0, '2018-01-20 16:00:13.937825', 2, 1),
-- (10, '2018-01-19', '10:02', '11:02', 'context', 'placeolder', 'albums/images/2018/01/20/23550950_10212662353168271_5668330830254242575_o_dP3SWpo.jpg', 1, 0, '2018-01-20 16:03:09.956288', 2, 1),
-- (11, '2018-01-20', '16:24', '18:24', 'description', 'mx', 'albums/images/2018/01/20/23550950_10212662353168271_5668330830254242575_o_cnFXSyY.jpg', 2, 0, '2018-01-20 22:25:13.398582', 1, 1),
-- (12, '2018-01-21', '19:50', '19:50', 'context', 'mx', 'albums/images/2018/01/21/23550950_10212662353168271_5668330830254242575_o.jpg', 0, 0, '2018-01-21 21:22:12.384877', 1, 3),
-- (13, '2018-01-21', '19:50', '19:50', 'context', 'mx', 'albums/images/2018/01/21/23550950_10212662353168271_5668330830254242575_o_MT3E2dY.jpg', 0, 0, '2018-01-21 21:22:51.979093', 1, 3),
-- (14, '2018-01-21', '09:27', '18:26', 'MDF', 'MX', 'albums/images/2018/01/22/23550950_10212662353168271_5668330830254242575_o.jpg', 8, 59, '2018-01-22 00:27:25.505399', 1, 1),
-- (15, '2018-01-22', '21:00', '06:00', 'esta es una descripcion mas fuerte que las demas por que es una prueba del editado', 'CDMX', 'albums/images/2018/01/22/Soldador.png', 9, 0, '2018-01-22 00:29:57.092157', 1, 1),
-- (16, '2018-01-22', '00:00', '00:00', 'el mismo contxto', 'Mexico', 'albums/images/2018/01/22/23550950_10212662353168271_5668330830254242575_o_TwbvEOC.jpg', 24, 0, '2018-01-22 23:20:24.804953', 1, 1),
-- (17, '2018-01-22', '00:00', '00:00', 'el mismo contxto', 'Mexico', 'albums/images/2018/01/22/23550950_10212662353168271_5668330830254242575_o_92Jjnk6.jpg', 24, 0, '2018-01-22 23:30:27.524521', 1, 1),
-- (18, '2018-01-22', '22:56', '19:56', 'pl,cdplecl', 'Mexico', 'albums/images/2018/01/23/23550950_10212662353168271_5668330830254242575_o.jpg', 21, 0, '2018-01-23 01:57:28.941819', 1, 1),
-- (19, '2018-01-23', '18:00', '19:57', 'este es un contexto', 'Mexico', 'albums/images/2018/01/23/Soldador.png', 1, 57, '2018-01-23 01:58:26.700728', 1, 1),
-- (20, '2018-01-29', '18:54', '18:54', 'kogfk', 'Mexico', 'albums/images/2018/01/30/wrench-512.png', 24, 0, '2018-01-30 00:55:11.450374', 1, 1),
-- (22, '2018-01-28', '16:07', '17:07', 'cskposdpo', 'Mexico', 'albums/images/2018/01/30/Soldador.png', 1, 0, '2018-01-30 22:07:28.625590', 1, 1),
-- (23, '2018-01-28', '00:00', '00:00', 'diaentero', 'lflf', 'albums/images/2018/01/30/Soldador_plYrUvt.png', 24, 0, '2018-01-30 22:11:10.663605', 4, 1),
-- (24, '2018-01-30', '07:35', '18:30', 'mexiorder', 'Mexico', 'albums/images/2018/01/30/wrench-512_Pi6z9Xd.png', 10, 55, '2018-01-30 22:17:31.207934', 4, 1);

-- --------------------------------------------------------

-- CREATE TABLE `work_order_workorder` (
--   `id` int(11) NOT NULL,
--   `opening_date` date NOT NULL,
--   `number` int(11) NOT NULL,
--   `description` longtext,
--   `is_active` tinyint(1) NOT NULL,
--   `created_at` datetime(6) NOT NULL,
--   `customer_id` int(11) NOT NULL
-- ) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --
-- -- Volcado de datos para la tabla `work_order_workorder`
-- --

-- INSERT INTO `work_order_workorder` (`id`, `opening_date`, `number`, `description`, `is_active`, `created_at`, `customer_id`) VALUES
-- (1, '2018-01-12', 1000, 'naoao', 1, '2018-01-12 02:39:39.234700', 1),
-- (2, '2018-01-13', 4000, 'arregalndo la casita', 0, '2018-01-13 21:24:50.090064', 1),
-- (3, '2018-01-13', 10000, 'ijoewijoew', 1, '2018-01-13 22:14:26.043537', 2);

