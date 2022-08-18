from functools import reduce

bus_branch = {
    'bus-100100100': ['branch153_or', 'branch154_or', 'branch157_or', 'branch158_or', 'branch159_ex', 'branch162_ex',
                      'branch163_ex', 'branch166_ex'], 'bus-10100100': ['branch8_or'],
    'bus-101100100': ['branch159_or', 'branch161_ex'], 'bus-102100100': ['branch160_or', 'branch161_or'],
    'bus-103100100': ['branch162_or', 'branch164_ex', 'branch165_ex', 'branch173_ex'],
    'bus-104100100': ['branch163_or', 'branch164_or', 'branch167_ex'],
    'bus-105100100': ['branch165_or', 'branch167_or', 'branch168_ex', 'branch169_ex', 'branch170_ex'],
    'bus-106100100': ['branch166_or', 'branch168_or', 'branch171_ex'],
    'bus-107100100': ['branch169_or', 'branch171_or', 'branch190_ex'],
    'bus-108100100': ['branch170_or', 'branch172_ex'], 'bus-109100100': ['branch172_or', 'branch174_ex'],
    'bus-1100100': ['branch0_ex', 'branch1_ex', 'branch186_ex'],
    'bus-110100100': ['branch173_or', 'branch174_or', 'branch175_ex', 'branch176_ex'],
    'bus-11100100': ['branch9_or', 'branch10_or', 'branch11_ex', 'branch15_ex'], 'bus-111100100': ['branch175_or'],
    'bus-112100100': ['branch176_or', 'branch191_ex'], 'bus-113100100': ['branch177_or', 'branch178_or'],
    'bus-114100100': ['branch179_or', 'branch181_ex'], 'bus-115100100': ['branch180_or', 'branch181_or'],
    'bus-116100100': ['branch182_or'], 'bus-117100100': ['branch183_or'],
    'bus-118100100': ['branch184_or', 'branch185_or'], 'bus-119100100': ['branch186_or'],
    'bus-120100100': ['branch187_or'],
    'bus-12100100': ['branch11_or', 'branch13_or', 'branch14_or', 'branch16_ex', 'branch19_ex', 'branch183_ex',
                     'branch192_ex'], 'bus-121100100': ['branch188_or'], 'bus-122100100': ['branch189_or'],
    'bus-123100100': ['branch190_or'], 'bus-124100100': ['branch191_or'],
    'bus-125100100': ['branch12_or', 'branch192_or'], 'bus-126100100': ['branch32_or', 'branch193_or'],
    'bus-13100100': ['branch15_or', 'branch17_ex'], 'bus-14100100': ['branch16_or', 'branch18_ex'],
    'bus-15100100': ['branch17_or', 'branch18_or', 'branch20_ex', 'branch25_ex', 'branch43_ex'],
    'bus-16100100': ['branch19_or', 'branch21_ex'],
    'bus-17100100': ['branch20_or', 'branch21_or', 'branch22_ex', 'branch35_ex', 'branch38_ex', 'branch177_ex'],
    'bus-18100100': ['branch22_or', 'branch23_ex'],
    'bus-19100100': ['branch23_or', 'branch24_ex', 'branch25_or', 'branch44_ex'],
    'bus-20100100': ['branch24_or', 'branch26_ex'], 'bus-2100100': ['branch0_or', 'branch12_ex'],
    'bus-21100100': ['branch26_or', 'branch27_ex'], 'bus-22100100': ['branch27_or', 'branch28_ex'],
    'bus-23100100': ['branch28_or', 'branch29_ex', 'branch30_ex', 'branch40_ex'],
    'bus-24100100': ['branch29_or', 'branch108_ex', 'branch110_ex'],
    'bus-25100100': ['branch30_or', 'branch31_ex', 'branch193_ex'], 'bus-26100100': ['branch31_or', 'branch37_ex'],
    'bus-27100100': ['branch32_ex', 'branch33_ex', 'branch42_ex', 'branch180_ex', 'branch187_ex'],
    'bus-28100100': ['branch33_or', 'branch34_ex'], 'bus-29100100': ['branch34_or', 'branch39_ex'],
    'bus-30100100': ['branch35_or', 'branch36_or', 'branch37_or', 'branch53_ex'],
    'bus-3100100': ['branch1_or', 'branch3_ex', 'branch13_ex'],
    'bus-31100100': ['branch38_or', 'branch39_or', 'branch41_ex'],
    'bus-32100100': ['branch40_or', 'branch41_or', 'branch42_or', 'branch178_ex', 'branch179_ex'],
    'bus-33100100': ['branch43_or', 'branch47_ex'],
    'bus-34100100': ['branch44_or', 'branch48_ex', 'branch49_ex', 'branch59_ex'],
    'bus-35100100': ['branch45_ex', 'branch46_ex'], 'bus-36100100': ['branch45_or', 'branch48_or'],
    'bus-37100100': ['branch46_or', 'branch47_or', 'branch49_or', 'branch50_ex', 'branch51_ex', 'branch52_ex'],
    'bus-38100100': ['branch50_or', 'branch53_or', 'branch95_ex'], 'bus-39100100': ['branch51_or', 'branch54_ex'],
    'bus-40100100': ['branch52_or', 'branch54_or', 'branch55_ex', 'branch56_ex'],
    'bus-4100100': ['branch2_ex', 'branch9_ex'], 'bus-41100100': ['branch55_or', 'branch57_ex'],
    'bus-42100100': ['branch56_or', 'branch57_or', 'branch65_ex', 'branch66_ex'],
    'bus-43100100': ['branch58_ex', 'branch59_or'], 'bus-44100100': ['branch58_or', 'branch60_ex'],
    'bus-45100100': ['branch60_or', 'branch61_ex', 'branch67_ex'],
    'bus-46100100': ['branch61_or', 'branch62_ex', 'branch63_ex'],
    'bus-47100100': ['branch62_or', 'branch64_ex', 'branch104_ex'], 'bus-48100100': ['branch63_or', 'branch68_ex'],
    'bus-49100100': ['branch64_or', 'branch65_or', 'branch66_or', 'branch67_or', 'branch68_or', 'branch69_ex',
                     'branch70_ex', 'branch74_ex', 'branch75_ex', 'branch97_ex', 'branch98_ex', 'branch105_ex'],
    'bus-50100100': ['branch69_or', 'branch80_ex'],
    'bus-5100100': ['branch2_or', 'branch3_or', 'branch4_ex', 'branch7_ex', 'branch10_ex'],
    'bus-51100100': ['branch70_or', 'branch71_ex', 'branch82_ex'], 'bus-52100100': ['branch71_or', 'branch72_ex'],
    'bus-53100100': ['branch72_or', 'branch73_ex'],
    'bus-54100100': ['branch73_or', 'branch74_or', 'branch75_or', 'branch76_ex', 'branch77_ex', 'branch83_ex',
                     'branch188_ex'], 'bus-55100100': ['branch76_or', 'branch78_ex', 'branch86_ex'],
    'bus-56100100': ['branch77_or', 'branch78_or', 'branch79_ex', 'branch81_ex', 'branch84_ex', 'branch85_ex'],
    'bus-57100100': ['branch79_or', 'branch80_or'], 'bus-58100100': ['branch81_or', 'branch82_or'],
    'bus-59100100': ['branch83_or', 'branch84_or', 'branch85_or', 'branch86_or', 'branch87_ex', 'branch88_ex',
                     'branch92_ex', 'branch189_ex'], 'bus-60100100': ['branch87_or', 'branch89_ex', 'branch90_ex'],
    'bus-6100100': ['branch4_or', 'branch5_ex'],
    'bus-61100100': ['branch88_or', 'branch89_or', 'branch91_ex', 'branch94_ex'],
    'bus-62100100': ['branch90_or', 'branch91_or', 'branch99_ex', 'branch100_ex'],
    'bus-63100100': ['branch92_or', 'branch93_ex'], 'bus-64100100': ['branch93_or', 'branch94_or', 'branch96_ex'],
    'bus-65100100': ['branch95_or', 'branch96_or', 'branch101_or', 'branch103_ex'],
    'bus-66100100': ['branch97_or', 'branch98_or', 'branch99_or', 'branch101_ex', 'branch102_ex'],
    'bus-67100100': ['branch100_or', 'branch102_or'],
    'bus-68100100': ['branch103_or', 'branch106_or', 'branch125_ex', 'branch182_ex'],
    'bus-69100100': ['branch104_or', 'branch105_or', 'branch106_ex', 'branch107_ex', 'branch115_ex', 'branch118_ex'],
    'bus-70100100': ['branch107_or', 'branch108_or', 'branch109_ex', 'branch113_ex', 'branch114_ex'],
    'bus-7100100': ['branch5_or', 'branch14_ex'], 'bus-71100100': ['branch109_or', 'branch111_ex', 'branch112_ex'],
    'bus-72100100': ['branch110_or', 'branch111_or'], 'bus-73100100': ['branch112_or'],
    'bus-74100100': ['branch113_or', 'branch116_ex'],
    'bus-75100100': ['branch114_or', 'branch115_or', 'branch116_or', 'branch119_ex', 'branch184_ex'],
    'bus-76100100': ['branch117_ex', 'branch185_ex'],
    'bus-77100100': ['branch117_or', 'branch118_or', 'branch119_or', 'branch120_ex', 'branch122_ex', 'branch123_ex',
                     'branch127_ex'], 'bus-78100100': ['branch120_or', 'branch121_ex'],
    'bus-79100100': ['branch121_or', 'branch124_ex'],
    'bus-80100100': ['branch122_or', 'branch123_or', 'branch124_or', 'branch126_ex', 'branch147_ex', 'branch150_ex',
                     'branch151_ex', 'branch152_ex'], 'bus-8100100': ['branch6_ex', 'branch7_or', 'branch36_ex'],
    'bus-81100100': ['branch125_or', 'branch126_or'], 'bus-82100100': ['branch127_or', 'branch128_ex', 'branch148_ex'],
    'bus-83100100': ['branch128_or', 'branch129_ex', 'branch130_ex'], 'bus-84100100': ['branch129_or', 'branch131_ex'],
    'bus-85100100': ['branch130_or', 'branch131_or', 'branch132_ex', 'branch134_ex', 'branch135_ex'],
    'bus-86100100': ['branch132_or', 'branch133_ex'], 'bus-87100100': ['branch133_or'],
    'bus-88100100': ['branch134_or', 'branch136_ex'],
    'bus-89100100': ['branch135_or', 'branch136_or', 'branch137_ex', 'branch138_ex', 'branch140_ex', 'branch141_ex'],
    'bus-90100100': ['branch137_or', 'branch138_or', 'branch139_ex'], 'bus-9100100': ['branch6_or', 'branch8_ex'],
    'bus-91100100': ['branch139_or', 'branch142_ex'],
    'bus-92100100': ['branch140_or', 'branch141_or', 'branch142_or', 'branch143_ex', 'branch144_ex', 'branch153_ex',
                     'branch160_ex'], 'bus-93100100': ['branch143_or', 'branch145_ex'],
    'bus-94100100': ['branch144_or', 'branch145_or', 'branch146_ex', 'branch149_ex', 'branch154_ex'],
    'bus-95100100': ['branch146_or', 'branch155_ex'],
    'bus-96100100': ['branch147_or', 'branch148_or', 'branch149_or', 'branch155_or', 'branch156_ex'],
    'bus-97100100': ['branch150_or', 'branch156_or'], 'bus-98100100': ['branch151_or', 'branch157_ex'],
    'bus-99100100': ['branch152_or', 'branch158_ex']}
bus_gen = {'bus-100100100': ['bus.100.gen'], 'bus-10100100': ['bus.10.gen'], 'bus-101100100': [''],
           'bus-102100100': [''], 'bus-103100100': ['bus.103.gen'], 'bus-104100100': ['bus.104.gen'],
           'bus-105100100': ['bus.105.gen'], 'bus-106100100': [''], 'bus-107100100': [''], 'bus-108100100': [''],
           'bus-109100100': [''], 'bus-1100100': [''], 'bus-110100100': ['bus.110.gen'], 'bus-11100100': [''],
           'bus-111100100': ['bus.111.gen'], 'bus-112100100': [''], 'bus-113100100': ['bus.113.gen'],
           'bus-114100100': [''], 'bus-115100100': [''], 'bus-116100100': ['bus.116.gen'], 'bus-117100100': [''],
           'bus-118100100': [''], 'bus-119100100': ['bus.119.gen'], 'bus-120100100': ['bus.120.gen'],
           'bus-12100100': ['bus.12.gen'], 'bus-121100100': ['bus.121.gen'], 'bus-122100100': ['bus.122.gen'],
           'bus-123100100': ['bus.123.gen'], 'bus-124100100': ['bus.124.gen'], 'bus-125100100': [''],
           'bus-126100100': [''], 'bus-13100100': [''], 'bus-14100100': [''], 'bus-15100100': ['bus.15.gen'],
           'bus-16100100': [''], 'bus-17100100': [''], 'bus-18100100': ['bus.18.gen'], 'bus-19100100': ['bus.19.gen'],
           'bus-20100100': [''], 'bus-2100100': [''], 'bus-21100100': [''], 'bus-22100100': [''], 'bus-23100100': [''],
           'bus-24100100': ['bus.24.gen'], 'bus-25100100': ['bus.25.gen'], 'bus-26100100': ['bus.26.gen'],
           'bus-27100100': [''], 'bus-28100100': [''], 'bus-29100100': [''], 'bus-30100100': [''], 'bus-3100100': [''],
           'bus-31100100': ['bus.31.gen'], 'bus-32100100': ['bus.32.gen'], 'bus-33100100': [''],
           'bus-34100100': ['bus.34.gen'], 'bus-35100100': [''], 'bus-36100100': ['bus.36.gen'], 'bus-37100100': [''],
           'bus-38100100': [''], 'bus-39100100': [''], 'bus-40100100': ['bus.40.gen'], 'bus-4100100': ['bus.4.gen'],
           'bus-41100100': [''], 'bus-42100100': ['bus.42.gen'], 'bus-43100100': [''], 'bus-44100100': [''],
           'bus-45100100': [''], 'bus-46100100': ['bus.46.gen'], 'bus-47100100': [''], 'bus-48100100': [''],
           'bus-49100100': ['bus.49.gen'], 'bus-50100100': [''], 'bus-5100100': [''], 'bus-51100100': [''],
           'bus-52100100': [''], 'bus-53100100': [''], 'bus-54100100': [''], 'bus-55100100': ['bus.55.gen'],
           'bus-56100100': ['bus.56.gen'], 'bus-57100100': [''], 'bus-58100100': [''], 'bus-59100100': [''],
           'bus-60100100': [''], 'bus-6100100': ['bus.6.gen'], 'bus-61100100': ['bus.61.gen'],
           'bus-62100100': ['bus.62.gen'], 'bus-63100100': [''], 'bus-64100100': [''], 'bus-65100100': ['bus.65.gen'],
           'bus-66100100': ['bus.66.gen'], 'bus-67100100': [''], 'bus-68100100': [''], 'bus-69100100': ['bus.69.gen'],
           'bus-70100100': ['bus.70.gen'], 'bus-7100100': [''], 'bus-71100100': [''], 'bus-72100100': ['bus.72.gen'],
           'bus-73100100': ['bus.73.gen'], 'bus-74100100': ['bus.74.gen'], 'bus-75100100': [''],
           'bus-76100100': ['bus.76.gen'], 'bus-77100100': ['bus.77.gen'], 'bus-78100100': [''], 'bus-79100100': [''],
           'bus-80100100': ['bus.80.gen'], 'bus-8100100': ['bus.8.gen'], 'bus-81100100': [''], 'bus-82100100': [''],
           'bus-83100100': [''], 'bus-84100100': [''], 'bus-85100100': ['bus.85.gen'], 'bus-86100100': [''],
           'bus-87100100': ['bus.87.gen'], 'bus-88100100': [''], 'bus-89100100': ['bus.89.gen'],
           'bus-90100100': ['bus.90.gen'], 'bus-9100100': [''], 'bus-91100100': ['bus.91.gen'],
           'bus-92100100': ['bus.92.gen'], 'bus-93100100': [''], 'bus-94100100': [''], 'bus-95100100': [''],
           'bus-96100100': [''], 'bus-97100100': [''], 'bus-98100100': [''], 'bus-99100100': ['bus.99.gen']}
bus_load = {'bus-100100100': ['bus.100.ld'], 'bus-10100100': [''], 'bus-101100100': ['bus.101.ld'],
            'bus-102100100': ['bus.102.ld'], 'bus-103100100': ['bus.103.ld'], 'bus-104100100': ['bus.104.ld'],
            'bus-105100100': ['bus.105.ld'], 'bus-106100100': ['bus.106.ld'], 'bus-107100100': ['bus.107.ld'],
            'bus-108100100': ['bus.108.ld'], 'bus-109100100': ['bus.109.ld'], 'bus-1100100': ['bus.1.ld'],
            'bus-110100100': ['bus.110.ld'], 'bus-11100100': ['bus.11.ld'], 'bus-111100100': [''],
            'bus-112100100': ['bus.112.ld'], 'bus-113100100': [''], 'bus-114100100': ['bus.114.ld'],
            'bus-115100100': ['bus.115.ld'], 'bus-116100100': [''], 'bus-117100100': ['bus.117.ld'],
            'bus-118100100': ['bus.118.ld'], 'bus-119100100': [''], 'bus-120100100': [''],
            'bus-12100100': ['bus.12.ld'], 'bus-121100100': [''], 'bus-122100100': [''], 'bus-123100100': [''],
            'bus-124100100': [''], 'bus-125100100': [''], 'bus-126100100': [''], 'bus-13100100': ['bus.13.ld'],
            'bus-14100100': ['bus.14.ld'], 'bus-15100100': ['bus.15.ld'], 'bus-16100100': ['bus.16.ld'],
            'bus-17100100': ['bus.17.ld'], 'bus-18100100': ['bus.18.ld'], 'bus-19100100': ['bus.19.ld'],
            'bus-20100100': ['bus.20.ld'], 'bus-2100100': ['bus.2.ld'], 'bus-21100100': ['bus.21.ld'],
            'bus-22100100': ['bus.22.ld'], 'bus-23100100': ['bus.23.ld'], 'bus-24100100': [''], 'bus-25100100': [''],
            'bus-26100100': [''], 'bus-27100100': ['bus.27.ld'], 'bus-28100100': ['bus.28.ld'],
            'bus-29100100': ['bus.29.ld'], 'bus-30100100': [''], 'bus-3100100': ['bus.3.ld'],
            'bus-31100100': ['bus.31.ld'], 'bus-32100100': ['bus.32.ld'], 'bus-33100100': ['bus.33.ld'],
            'bus-34100100': ['bus.34.ld'], 'bus-35100100': ['bus.35.ld'], 'bus-36100100': ['bus.36.ld'],
            'bus-37100100': [''], 'bus-38100100': [''], 'bus-39100100': ['bus.39.ld'], 'bus-40100100': ['bus.40.ld'],
            'bus-4100100': ['bus.4.ld'], 'bus-41100100': ['bus.41.ld'], 'bus-42100100': ['bus.42.ld'],
            'bus-43100100': ['bus.43.ld'], 'bus-44100100': ['bus.44.ld'], 'bus-45100100': ['bus.45.ld'],
            'bus-46100100': ['bus.46.ld'], 'bus-47100100': ['bus.47.ld'], 'bus-48100100': ['bus.48.ld'],
            'bus-49100100': ['bus.49.ld'], 'bus-50100100': ['bus.50.ld'], 'bus-5100100': [''],
            'bus-51100100': ['bus.51.ld'], 'bus-52100100': ['bus.52.ld'], 'bus-53100100': ['bus.53.ld'],
            'bus-54100100': ['bus.54.ld'], 'bus-55100100': ['bus.55.ld'], 'bus-56100100': ['bus.56.ld'],
            'bus-57100100': ['bus.57.ld'], 'bus-58100100': ['bus.58.ld'], 'bus-59100100': ['bus.59.ld'],
            'bus-60100100': ['bus.60.ld'], 'bus-6100100': ['bus.6.ld'], 'bus-61100100': [''],
            'bus-62100100': ['bus.62.ld'], 'bus-63100100': [''], 'bus-64100100': [''], 'bus-65100100': [''],
            'bus-66100100': ['bus.66.ld'], 'bus-67100100': ['bus.67.ld'], 'bus-68100100': [''], 'bus-69100100': [''],
            'bus-70100100': ['bus.70.ld'], 'bus-7100100': ['bus.7.ld'], 'bus-71100100': [''], 'bus-72100100': [''],
            'bus-73100100': [''], 'bus-74100100': ['bus.74.ld'], 'bus-75100100': ['bus.75.ld'],
            'bus-76100100': ['bus.76.ld'], 'bus-77100100': ['bus.77.ld'], 'bus-78100100': ['bus.78.ld'],
            'bus-79100100': ['bus.79.ld'], 'bus-80100100': ['bus.80.ld'], 'bus-8100100': [''], 'bus-81100100': [''],
            'bus-82100100': ['bus.82.ld'], 'bus-83100100': ['bus.83.ld'], 'bus-84100100': ['bus.84.ld'],
            'bus-85100100': ['bus.85.ld'], 'bus-86100100': ['bus.86.ld'], 'bus-87100100': [''],
            'bus-88100100': ['bus.88.ld'], 'bus-89100100': [''], 'bus-90100100': ['bus.90.ld'], 'bus-9100100': [''],
            'bus-91100100': [''], 'bus-92100100': ['bus.92.ld'], 'bus-93100100': ['bus.93.ld'],
            'bus-94100100': ['bus.94.ld'], 'bus-95100100': ['bus.95.ld'], 'bus-96100100': ['bus.96.ld'],
            'bus-97100100': ['bus.97.ld'], 'bus-98100100': ['bus.98.ld'], 'bus-99100100': ['']}
bus_names = set([v for v in bus_branch.keys()])
branch_names = set(
    [v.split('_')[0] for v in reduce(lambda a, b: a + b, [v for v in bus_branch.values()])])
gen_names = set(
    [v.split('_')[0] for v in reduce(lambda a, b: a + b, [v for v in bus_gen.values()]) if '' != v])
load_names = set(
    [v.split('_')[0] for v in reduce(lambda a, b: a + b, [v for v in bus_load.values()]) if '' != v])


def get_dict():
    # 观测空间观测到一共有 126 个 bus，编号 0 ~ 125
    id2name = {i: name for i, name in enumerate(bus_names)}
    count = len(id2name)

    # 观测空间观测到一共有 194 个 branch，对应起始端编号为 126 ~ 319。（配置文件中实际只给了 185 个 branch 的相关约束值）
    id2name.update({count + i: f"{name}_or" for i, name in enumerate(branch_names)})
    count = len(id2name)

    # 末端编号为 320 ~ 513
    id2name.update({count + i: f"{name}_ex" for i, name in enumerate(branch_names)})
    count = len(id2name)

    # 54 个发电机组，编号为 514 ~ 567
    id2name.update({count + i: name for i, name in enumerate(gen_names)})
    count = len(id2name)

    # 91 个负载，编号为 568 ~ 658
    id2name.update({count + i: name for i, name in enumerate(load_names)})
    count = len(id2name)

    name2id = {v: k for k, v in id2name.items()}

    return id2name, name2id


if __name__ == "__main__":
    id2name, name2id = get_dict()
