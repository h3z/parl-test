from parl_baseline.graph.map_utils import  *

# TODO 这里需要确认一下为什么 bus_'branch'中提到的 'branch'有 194 个 'branch', 但是观测空间和静态配置文件中都只有 185 个

white_list_random_disconnection = ['branch43', 'branch44', 'branch113', 'branch114', 'branch115', 'branch118',
                                   'branch66', 'branch75', 'branch85', 'branch98', 'branch123', 'branch138',
                                   'branch141']

ln_thermal_limit = [313.92, 462.14, 889.01, 537.54, 583.39, 500.21, 340.29, 332.76, 411.88, 494.58, 588.21, 435.0,
                    154.59, 327.68, 416.04, 338.65, 327.49, 374.02, 370.94, 1110.62, 550.22, 592.95, 524.57, 480.72,
                    370.68, 346.75, 464.19, 660.54, 1585.64, 448.65, 536.74, 650.22, 235.09, 2116.18, 1071.66, 568.59,
                    548.97, 667.71, 393.76, 329.76, 505.94, 407.59, 582.89, 555.51, 599.72, 697.28, 1815.1, 1874.33,
                    1990.32, 5032.53, 2338.87, 972.76, 915.44, 890.04, 297.88, 580.58, 689.74, 806.95, 707.04, 415.57,
                    673.69, 710.87, 645.34, 638.31, 829.28, 429.4, 404.84, 241.6, 354.29, 530.04, 495.36, 403.21, 258.2,
                    974.56, 785.51, 800.9, 519.76, 810.43, 529.92, 303.62, 278.99, 243.14, 356.43, 354.18, 353.73,
                    284.72, 210.79, 335.84, 1009.7, 6355.77, 2075.32, 771.7, 641.42, 382.77, 455.75, 498.24, 4372.12,
                    524.4, 420.05, 715.12, 528.49, 1467.84, 1002.15, 512.97, 1016.97, 463.95, 439.73, 403.86, 456.4,
                    444.41, 705.01, 327.2, 455.05, 348.73, 380.07, 148.98, 299.2, 3347.97, 1285.32, 1279.9, 637.34,
                    962.3, 774.19, 426.1, 433.27, 670.91, 724.17, 785.4, 353.95, 551.84, 599.4, 1202.41, 321.33, 927.52,
                    832.59, 723.43, 629.9, 1208.54, 750.96, 516.56, 1174.53, 669.77, 939.06, 1137.56, 403.43, 1548.73,
                    938.07, 953.0, 1220.32, 1127.6, 371.19, 649.98, 470.15, 1861.8, 646.35, 296.3, 351.13, 525.05,
                    673.05, 427.39, 434.37, 841.91, 414.47, 649.23, 735.1, 875.21, 411.04, 1641.13, 1088.42, 432.49,
                    278.21, 273.69, 225.8, 365.48, 488.46, 655.39, 866.37, 522.05, 650.22, 882.74, 768.44, 861.3,
                    1641.13, 435.0, 536.74]

ln_name = ['branch0', 'branch1', 'branch2', 'branch3', 'branch4', 'branch5', 'branch6', 'branch8', 'branch9',
           'branch10', 'branch11', 'branch12', 'branch13', 'branch14', 'branch15', 'branch16', 'branch17', 'branch18',
           'branch19', 'branch20', 'branch21', 'branch22', 'branch23', 'branch24', 'branch25', 'branch26', 'branch27',
           'branch28', 'branch29', 'branch30', 'branch32', 'branch33', 'branch34', 'branch36', 'branch37', 'branch38',
           'branch39', 'branch40', 'branch41', 'branch42', 'branch43', 'branch44', 'branch45', 'branch46', 'branch47',
           'branch48', 'branch49', 'branch51', 'branch52', 'branch53', 'branch54', 'branch55', 'branch56', 'branch57',
           'branch58', 'branch59', 'branch60', 'branch61', 'branch62', 'branch63', 'branch64', 'branch65', 'branch66',
           'branch67', 'branch68', 'branch69', 'branch70', 'branch71', 'branch72', 'branch73', 'branch74', 'branch75',
           'branch76', 'branch77', 'branch78', 'branch79', 'branch80', 'branch81', 'branch82', 'branch83', 'branch84',
           'branch85', 'branch86', 'branch87', 'branch88', 'branch89', 'branch90', 'branch91', 'branch93', 'branch95',
           'branch96', 'branch97', 'branch98', 'branch99', 'branch100', 'branch102', 'branch103', 'branch104',
           'branch105', 'branch107', 'branch108', 'branch109', 'branch110', 'branch111', 'branch112', 'branch113',
           'branch114', 'branch115', 'branch116', 'branch117', 'branch118', 'branch119', 'branch120', 'branch121',
           'branch122', 'branch123', 'branch124', 'branch125', 'branch127', 'branch128', 'branch129', 'branch130',
           'branch131', 'branch132', 'branch133', 'branch134', 'branch135', 'branch136', 'branch137', 'branch138',
           'branch139', 'branch140', 'branch141', 'branch142', 'branch143', 'branch144', 'branch145', 'branch146',
           'branch147', 'branch148', 'branch149', 'branch150', 'branch151', 'branch152', 'branch153', 'branch154',
           'branch155', 'branch156', 'branch157', 'branch158', 'branch159', 'branch160', 'branch161', 'branch162',
           'branch163', 'branch164', 'branch165', 'branch166', 'branch167', 'branch168', 'branch169', 'branch170',
           'branch171', 'branch172', 'branch173', 'branch174', 'branch175', 'branch176', 'branch177', 'branch178',
           'branch179', 'branch180', 'branch181', 'branch182', 'branch183', 'branch184', 'branch185', 'branch186',
           'branch187', 'branch188', 'branch189', 'branch190', 'branch191', 'branch192', 'branch193']

is_white_list_random_disconnection = [i in white_list_random_disconnection for i in ln_name]

obs_branch_name2id = {name: i for i, name in enumerate(ln_name)}


def static_and_obs(obs):
    assert (len(ln_name) == 185)
    assert (len(ln_thermal_limit) == 185)

    from_obs = obs_map_to(obs,
                          ['a_ex', 'a_or', 'p_ex', 'p_or', 'q_ex', 'q_or', 'rho', 'steps_to_reconnect_line', 'v_ex',
                           'v_or', 'count_soft_overflow_steps', 'line_status'], obs_branch_name2id)
    from_obs.update({
        'ln_thermal_limit': map_to(ln_thermal_limit, obs_branch_name2id),
        'white_list_random_disconnection': map_to(is_white_list_random_disconnection, obs_branch_name2id),
    })
    return from_obs
