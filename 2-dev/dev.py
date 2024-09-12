#### SSTOOLS4MC MAIN PROGRAM ####
####  DEVELOPED BY: NGDPLNK  ####
#################################
####      PROGRAM INFO       ####
SSVERSION = 'v24.09.12F-dev'
CHANNEL = 'dev'
YEAR = '2024'
CHANGELOG_ENG = '- SSTools4MC Launcher v1.4 Released!'
CHANGELOG_SPA = '- Se lanzó SSTools4MC Launcher v1.4!'
HELPERS = 'Helpers:\n@LegalizeNuclearBombs\n@naicoooossj'
NEEDED_MODULES = {
    # 'Module': 'Function (if needed)'
    'requests': '',
    'termcolor': 'colored'
}
#################################
### MINECRAFT VERSIONS ###

## 92 STABLE VERSIONS ADDED (1.0.0-tominecon - 1.21.1)
# LAST UPDATED: 10/08/2024
MC_STABLE = {
    # "Version name": "Download link"
    "1.0.0-tominecon": "https://vault.omniarchive.uk/archive/java/misc/1.0.0-tominecon-server.jar",
    "1.0.0": "https://files.betacraft.uk/server-archive/release/1.0/1.0.0.jar",
    "1.0.1": "https://files.betacraft.uk/server-archive/release/1.0/1.0.1.jar",
    "1.1": "https://files.betacraft.uk/server-archive/release/1.1/1.1.jar",
    "1.2.1": "https://files.betacraft.uk/server-archive/release/1.2/1.2.1.jar",
    "1.2.2": "https://files.betacraft.uk/server-archive/release/1.2/1.2.2.jar",
    "1.2.3": "https://files.betacraft.uk/server-archive/release/1.2/1.2.3.jar",
    "1.2.4": "https://files.betacraft.uk/server-archive/release/1.2/1.2.4.jar",
    "1.2.5": "https://piston-data.mojang.com/v1/objects/d8321edc9470e56b8ad5c67bbd16beba25843336/server.jar",
    "1.3.1": "https://piston-data.mojang.com/v1/objects/82563ce498bfc1fc8a2cb5bf236f7da86a390646/server.jar",
    "1.3.2": "https://piston-data.mojang.com/v1/objects/3de2ae6c488135596e073a9589842800c9f53bfe/server.jar",
    "1.4.2": "https://piston-data.mojang.com/v1/objects/5be700523a729bb78ef99206fb480a63dcd09825/server.jar",
    "1.4.4": "https://piston-data.mojang.com/v1/objects/4215dcadb706508bf9d6d64209a0080b9cee9e71/server.jar",
    "1.4.5": "https://piston-data.mojang.com/v1/objects/c12fd88a8233d2c517dbc8196ba2ae855f4d36ea/server.jar",
    "1.4.6": "https://piston-data.mojang.com/v1/objects/a0aeb5709af5f2c3058c1cf0dc6b110a7a61278c/server.jar",
    "1.4.7": "https://piston-data.mojang.com/v1/objects/2f0ec8efddd2f2c674c77be9ddb370b727dec676/server.jar",
    "1.5": "https://piston-data.mojang.com/v1/objects/aedad5159ef56d69c5bcf77ed141f53430af43c3/server.jar",
    "1.5.1": "https://piston-data.mojang.com/v1/objects/d07c71ee2767dabb79fb32dad8162e1b854d5324/server.jar",
    "1.5.2": "https://piston-data.mojang.com/v1/objects/f9ae3f651319151ce99a0bfad6b34fa16eb6775f/server.jar",
    "1.6.1": "https://piston-data.mojang.com/v1/objects/0252918a5f9d47e3c6eb1dfec02134d1374a89b4/server.jar",
    "1.6.2": "https://piston-data.mojang.com/v1/objects/01b6ea555c6978e6713e2a2dfd7fe19b1449ca54/server.jar",
    "1.6.4-original": "https://files.betacraft.uk/server-archive/release/1.6/1.6.4-201309191549.jar",
    "1.6.4-reupload": "https://piston-data.mojang.com/v1/objects/050f93c1f3fe9e2052398f7bd6aca10c63d64a87/server.jar",
    "1.7.2": "https://piston-data.mojang.com/v1/objects/3716cac82982e7c2eb09f83028b555e9ea606002/server.jar",
    "1.7.4": "https://piston-data.mojang.com/v1/objects/61220311cef80aecc4cd8afecd5f18ca6b9461ff/server.jar",
    "1.7.5-original": "https://vault.omniarchive.uk/archive/java/server-release/1.7/1.7.5-02260922.jar",
    "1.7.5-reupload": "https://piston-data.mojang.com/v1/objects/e1d557b2e31ea881404e41b05ec15c810415e060/server.jar",
    "1.7.6": "https://piston-data.mojang.com/v1/objects/41ea7757d4d7f74b95fc1ac20f919a8e521e910c/server.jar",
    "1.7.7": "https://piston-data.mojang.com/v1/objects/a6ffc1624da980986c6cc12a1ddc79ab1b025c62/server.jar",
    "1.7.8": "https://piston-data.mojang.com/v1/objects/c69ebfb84c2577661770371c4accdd5f87b8b21d/server.jar",
    "1.7.9": "https://piston-data.mojang.com/v1/objects/4cec86a928ec171fdc0c6b40de2de102f21601b5/server.jar",
    "1.7.10": "https://piston-data.mojang.com/v1/objects/952438ac4e01b4d115c5fc38f891710c4941df29/server.jar",
    "1.8": "https://piston-data.mojang.com/v1/objects/a028f00e678ee5c6aef0e29656dca091b5df11c7/server.jar",
    "1.8.1": "https://piston-data.mojang.com/v1/objects/68bfb524888f7c0ab939025e07e5de08843dac0f/server.jar",
    "1.8.2": "https://piston-data.mojang.com/v1/objects/a37bdd5210137354ed1bfe3dac0a5b77fe08fe2e/server.jar",
    "1.8.3": "https://piston-data.mojang.com/v1/objects/163ba351cb86f6390450bb2a67fafeb92b6c0f2f/server.jar",
    "1.8.4": "https://piston-data.mojang.com/v1/objects/dd4b5eba1c79500390e0b0f45162fa70d38f8a3d/server.jar",
    "1.8.5": "https://piston-data.mojang.com/v1/objects/ea6dd23658b167dbc0877015d1072cac21ab6eee/server.jar",
    "1.8.6": "https://piston-data.mojang.com/v1/objects/2bd44b53198f143fb278f8bec3a505dad0beacd2/server.jar",
    "1.8.7": "https://piston-data.mojang.com/v1/objects/35c59e16d1f3b751cd20b76b9b8a19045de363a9/server.jar",
    "1.8.8": "https://piston-data.mojang.com/v1/objects/5fafba3f58c40dc51b5c3ca72a98f62dfdae1db7/server.jar",
    "1.8.9": "https://piston-data.mojang.com/v1/objects/b58b2ceb36e01bcd8dbf49c8fb66c55a9f0676cd/server.jar",
    "1.9": "https://piston-data.mojang.com/v1/objects/b4d449cf2918e0f3bd8aa18954b916a4d1880f0d/server.jar",
    "1.9.1": "https://piston-data.mojang.com/v1/objects/bf95d9118d9b4b827f524c878efd275125b56181/server.jar",
    "1.9.2": "https://piston-data.mojang.com/v1/objects/2b95cc7b136017e064c46d04a5825fe4cfa1be30/server.jar",
    "1.9.3": "https://piston-data.mojang.com/v1/objects/8e897b6b6d784f745332644f4d104f7a6e737ccf/server.jar",
    "1.9.4": "https://piston-data.mojang.com/v1/objects/edbb7b1758af33d365bf835eb9d13de005b1e274/server.jar",
    "1.10": "https://piston-data.mojang.com/v1/objects/a96617ffdf5dabbb718ab11a9a68e50545fc5bee/server.jar",
    "1.10.1": "https://piston-data.mojang.com/v1/objects/cb4c6f9f51a845b09a8861cdbe0eea3ff6996dee/server.jar",
    "1.10.2": "https://piston-data.mojang.com/v1/objects/3d501b23df53c548254f5e3f66492d178a48db63/server.jar",
    "1.11": "https://piston-data.mojang.com/v1/objects/48820c84cb1ed502cb5b2fe23b8153d5e4fa61c0/server.jar",
    "1.11.1": "https://piston-data.mojang.com/v1/objects/1f97bd101e508d7b52b3d6a7879223b000b5eba0/server.jar",
    "1.11.2": "https://piston-data.mojang.com/v1/objects/f00c294a1576e03fddcac777c3cf4c7d404c4ba4/server.jar",
    "1.12": "https://piston-data.mojang.com/v1/objects/8494e844e911ea0d63878f64da9dcc21f53a3463/server.jar",
    "1.12.1": "https://piston-data.mojang.com/v1/objects/561c7b2d54bae80cc06b05d950633a9ac95da816/server.jar",
    "1.12.2": "https://piston-data.mojang.com/v1/objects/886945bfb2b978778c3a0288fd7fab09d315b25f/server.jar",
    "1.13": "https://piston-data.mojang.com/v1/objects/d0caafb8438ebd206f99930cfaecfa6c9a13dca0/server.jar",
    "1.13.1": "https://piston-data.mojang.com/v1/objects/fe123682e9cb30031eae351764f653500b7396c9/server.jar",
    "1.13.2": "https://piston-data.mojang.com/v1/objects/3737db93722a9e39eeada7c27e7aca28b144ffa7/server.jar",
    "1.14": "https://piston-data.mojang.com/v1/objects/f1a0073671057f01aa843443fef34330281333ce/server.jar",
    "1.14.1": "https://piston-data.mojang.com/v1/objects/ed76d597a44c5266be2a7fcd77a8270f1f0bc118/server.jar",
    "1.14.2": "https://piston-data.mojang.com/v1/objects/808be3869e2ca6b62378f9f4b33c946621620019/server.jar",
    "1.14.3": "https://piston-data.mojang.com/v1/objects/d0d0fe2b1dc6ab4c65554cb734270872b72dadd6/server.jar",
    "1.14.4": "https://piston-data.mojang.com/v1/objects/3dc3d84a581f14691199cf6831b71ed1296a9fdf/server.jar",
    "1.15": "https://piston-data.mojang.com/v1/objects/e9f105b3c5c7e85c7b445249a93362a22f62442d/server.jar",
    "1.15.1": "https://piston-data.mojang.com/v1/objects/4d1826eebac84847c71a77f9349cc22afd0cf0a1/server.jar",
    "1.15.2": "https://piston-data.mojang.com/v1/objects/bb2b6b1aefcd70dfd1892149ac3a215f6c636b07/server.jar",
    "1.16-original": "https://piston-data.mojang.com/v1/objects/7361a24df069a06748844cc7483c35d4abd2d80c/server.jar",
    "1.16-reupload": "https://piston-data.mojang.com/v1/objects/a0d03225615ba897619220e256a266cb33a44b6b/server.jar",
    "1.16.1": "https://piston-data.mojang.com/v1/objects/a412fd69db1f81db3f511c1463fd304675244077/server.jar",
    "1.16.2": "https://piston-data.mojang.com/v1/objects/c5f6fb23c3876461d46ec380421e42b289789530/server.jar",
    "1.16.3": "https://piston-data.mojang.com/v1/objects/f02f4473dbf152c23d7d484952121db0b36698cb/server.jar",
    "1.16.4": "https://piston-data.mojang.com/v1/objects/35139deedbd5182953cf1caa23835da59ca3d7cd/server.jar",
    "1.16.5": "https://piston-data.mojang.com/v1/objects/1b557e7b033b583cd9f66746b7a9ab1ec1673ced/server.jar",
    "1.17": "https://piston-data.mojang.com/v1/objects/0a269b5f2c5b93b1712d0f5dc43b6182b9ab254e/server.jar",
    "1.17.1": "https://piston-data.mojang.com/v1/objects/a16d67e5807f57fc4e550299cf20226194497dc2/server.jar",
    "1.18": "https://piston-data.mojang.com/v1/objects/3cf24a8694aca6267883b17d934efacc5e44440d/server.jar",
    "1.18.1": "https://piston-data.mojang.com/v1/objects/125e5adf40c659fd3bce3e66e67a16bb49ecc1b9/server.jar",
    "1.18.2": "https://piston-data.mojang.com/v1/objects/c8f83c5655308435b3dcf03c06d9fe8740a77469/server.jar",
    "1.19": "https://piston-data.mojang.com/v1/objects/e00c4052dac1d59a1188b2aa9d5a87113aaf1122/server.jar",
    "1.19.1": "https://piston-data.mojang.com/v1/objects/8399e1211e95faa421c1507b322dbeae86d604df/server.jar",
    "1.19.2": "https://piston-data.mojang.com/v1/objects/f69c284232d7c7580bd89a5a4931c3581eae1378/server.jar",
    "1.19.3": "https://piston-data.mojang.com/v1/objects/c9df48efed58511cdd0213c56b9013a7b5c9ac1f/server.jar",
    "1.19.4": "https://piston-data.mojang.com/v1/objects/8f3112a1049751cc472ec13e397eade5336ca7ae/server.jar",
    "1.20": "https://piston-data.mojang.com/v1/objects/15c777e2cfe0556eef19aab534b186c0c6f277e1/server.jar",
    "1.20.1": "https://piston-data.mojang.com/v1/objects/84194a2f286ef7c14ed7ce0090dba59902951553/server.jar",
    "1.20.2": "https://piston-data.mojang.com/v1/objects/5b868151bd02b41319f54c8d4061b8cae84e665c/server.jar",
    "1.20.3": "https://piston-data.mojang.com/v1/objects/4fb536bfd4a83d61cdbaf684b8d311e66e7d4c49/server.jar",
    "1.20.4": "https://piston-data.mojang.com/v1/objects/8dd1a28015f51b1803213892b50b7b4fc76e594d/server.jar",
    "1.20.5": "https://piston-data.mojang.com/v1/objects/79493072f65e17243fd36a699c9a96b4381feb91/server.jar",
    "1.20.6": "https://piston-data.mojang.com/v1/objects/145ff0858209bcfc164859ba735d4199aafa1eea/server.jar",
    "1.21": "https://piston-data.mojang.com/v1/objects/450698d1863ab5180c25d7c804ef0fe6369dd1ba/server.jar",
    "1.21.1": "https://piston-data.mojang.com/v1/objects/59353fb40c36d304f2035d51e7d6e6baa98dc05c/server.jar"
}

## 612 SNAPSHOT VERSIONS ADDED (1.3 - 24w37a)
# LAST UPDATED: 12/09/2024
MC_SNAPSHOT = {
    # "Version name": "Download link"
    "1.3": "https://piston-data.mojang.com/v1/objects/cb21a9aaaf599c94dd7fa1b777b2f0cc37a776c7/server.jar",
    "1.4": "https://piston-data.mojang.com/v1/objects/9470a2bb0fcb8a426328441a01dba164fbbe52c9/server.jar",
    "1.4.1": "https://piston-data.mojang.com/v1/objects/baa4e4a7adc3dc9fbfc5ea36f0777b68c9eb7f4a/server.jar",
    "1.4.3": "https://piston-data.mojang.com/v1/objects/9be68adf6e80721975df12f2445fa24617328d18/server.jar",
    "1.5": "https://piston-data.mojang.com/v1/objects/aedad5159ef56d69c5bcf77ed141f53430af43c3/server.jar",
    "13w16a": "https://piston-data.mojang.com/v1/objects/dd76b63bad493e42b303dd8952c240f330251760/server.jar",
    "13w16b": "https://piston-data.mojang.com/v1/objects/c125111764b5774403ff2183debbb9da4805a64f/server.jar",
    "13w17a": "https://piston-data.mojang.com/v1/objects/48ece561c3512b2f9c0915dad7c3cb65560ceb39/server.jar",
    "13w18a": "https://piston-data.mojang.com/v1/objects/6084eae41c6e28d58fe8a1ee4ab4389a392f0139/server.jar",
    "13w18b": "https://piston-data.mojang.com/v1/objects/af7fd5e8cdc610f1e533ba7963bc39de422df1b6/server.jar",
    "13w18c": "https://piston-data.mojang.com/v1/objects/3f8dc565567174d777a416f979901e0fee010d2a/server.jar",
    "13w19a": "https://piston-data.mojang.com/v1/objects/17997ee2d9a3ad1070a74707f58ebb3e3a46ae10/server.jar",
    "13w21a": "https://piston-data.mojang.com/v1/objects/a04b6f0349b8de64c68a9311b4eaff478e37b558/server.jar",
    "13w21b": "https://piston-data.mojang.com/v1/objects/f5236a7628c74c22c33f57b50cb755598042aa5b/server.jar",
    "13w22a": "https://piston-data.mojang.com/v1/objects/94b99928dccee27ad9b1d90bd00e8f68f38f92e4/server.jar",
    "13w23a": "https://piston-data.mojang.com/v1/objects/b26a278856a6a4703054ad266b79b1ef397676c2/server.jar",
    "13w23b": "https://piston-data.mojang.com/v1/objects/b6b627c0a5fe9f53a22892f21c473e19617c1c0d/server.jar",
    "13w24a": "https://piston-data.mojang.com/v1/objects/d0f1eb0455c1bc3f73d5fc7252e282fd614f1f5b/server.jar",
    "13w24b": "https://piston-data.mojang.com/v1/objects/9c312da9bdcc562dc57e235a7a56900148c77f8d/server.jar",
    "13w25a": "https://piston-data.mojang.com/v1/objects/e1c2e7376fe489c5eba744b010993c402ab3f3f2/server.jar",
    "13w25b": "https://piston-data.mojang.com/v1/objects/9f7f205d7c00098d9aa6abd67ce4f93d0eeddcd7/server.jar",
    "13w25c": "https://piston-data.mojang.com/v1/objects/0f21dbd39728a50843d1b20cf832f26aaada353d/server.jar",
    "13w26a": "https://piston-data.mojang.com/v1/objects/bafe11faf3419c8813beb948e353912239d50bc1/server.jar",
    "1.6": "https://piston-data.mojang.com/v1/objects/ee6d5161ac28eef285df571dc1235d48f03c3e88/server.jar",
    "13w36a": "https://piston-data.mojang.com/v1/objects/8453f031175bac1a92db000befd14f70c8df8fb7/server.jar",
    "13w36b": "https://piston-data.mojang.com/v1/objects/2b6cdcd2df82ca8f04c1c2c7d77faf4cd25151ea/server.jar",
    "13w37a": "https://piston-data.mojang.com/v1/objects/c3d3d936394b35f20b871b140f5a8e6079822e51/server.jar",
    "1.6.3": "https://piston-data.mojang.com/v1/objects/5a4c69bdf7c4a9aa9580096805d8497ba7721e05/server.jar",
    "13w37b": "https://piston-data.mojang.com/v1/objects/f6322a6791bbeabac94cbaa1cf9b779ad88b120f/server.jar",
    "13w38a": "https://piston-data.mojang.com/v1/objects/627585cdb9386e7f05cdfb8f092e5a303d4fd5f3/server.jar",
    "13w38b": "https://piston-data.mojang.com/v1/objects/82588f79a6a61c4c4289a9dc60b7b7b3fedaead9/server.jar",
    "13w38c": "https://piston-data.mojang.com/v1/objects/03081b4b569174ec68ef9cdd574ee4feca05dea5/server.jar",
    "13w39a": "https://piston-data.mojang.com/v1/objects/10e8687a623cb3def606fa3855aaed5ef79aac66/server.jar",
    "13w39b": "https://piston-data.mojang.com/v1/objects/1db7286055aeb35c709d98ace1c9cdc739206d5a/server.jar",
    "13w41a": "https://piston-data.mojang.com/v1/objects/fbe939a8a9246db801428e33a1c53506af637247/server.jar",
    "13w41b": "https://piston-data.mojang.com/v1/objects/d0f1808505d59bd69c47d8e0ce01dc5936d34c34/server.jar",
    "13w42a": "https://piston-data.mojang.com/v1/objects/d7007e5f46bb1ad4f4d38dc8cd2ea54898c6cccb/server.jar",
    "13w42b": "https://piston-data.mojang.com/v1/objects/1416ebe3d6e6aa62eaae305ce542c39b7dfcb2b9/server.jar",
    "13w43a": "https://piston-data.mojang.com/v1/objects/0fd72957ddbedd604d2bdf155dd03c8501c48f48/server.jar",
    "1.7": "https://piston-data.mojang.com/v1/objects/3f031ab8b9cafedeb822febe89d271b72565712c/server.jar",
    "1.7.1": "https://piston-data.mojang.com/v1/objects/d26d79675147253b7a35dd32dc5dbba0af1be7e2/server.jar",
    "13w47a": "https://piston-data.mojang.com/v1/objects/f3210daa0a05a88b8b8edadfc8af385ff3f88987/server.jar",
    "13w47b": "https://piston-data.mojang.com/v1/objects/7c1b69de43b6edf1d20f5030b88df78fd08ad8c7/server.jar",
    "13w47c": "https://piston-data.mojang.com/v1/objects/5cf618125f87452e665f0097171d089f73dc7e1c/server.jar",
    "13w47d": "https://piston-data.mojang.com/v1/objects/28982e580acf736120a4f1c3e7418e2a8daa3a8c/server.jar",
    "13w47e": "https://piston-data.mojang.com/v1/objects/0f08e81b37b2c06ead45f498a7c8efa10a02633a/server.jar",
    "13w48a": "https://piston-data.mojang.com/v1/objects/8f43e47eb288d3485f7825c422e9c5bcaf6418af/server.jar",
    "13w48b": "https://piston-data.mojang.com/v1/objects/9ab8a06fe77ed7f553ae3427d304e9f55de339d9/server.jar",
    "13w49a": "https://piston-data.mojang.com/v1/objects/164c350e011f491f6e12861ee4988ef2ccecfe0e/server.jar",
    "14w02a": "https://piston-data.mojang.com/v1/objects/b908214fb99891c4f1e77c21b1fcbe4f7cafdd58/server.jar",
    "14w02b": "https://piston-data.mojang.com/v1/objects/2f873b2fd721c9ed5ef51e80df96d10e5390ee9f/server.jar",
    "14w02c": "https://piston-data.mojang.com/v1/objects/c844eb4e22c6c0a3b87835fc61a508caeeced1f9/server.jar",
    "14w03a": "https://piston-data.mojang.com/v1/objects/5cbd5319a7b1198f049286d443148f1b88ff7bc7/server.jar",
    "14w03b": "https://piston-data.mojang.com/v1/objects/b8bee8cbf485aad0be9789fe58ab266d8fe82215/server.jar",
    "14w04a": "https://piston-data.mojang.com/v1/objects/bd483603d1b07d3ce3fde76a35abfb0489933d72/server.jar",
    "14w04b": "https://piston-data.mojang.com/v1/objects/7af6befa241678d09d4031fed5578785dd3c126d/server.jar",
    "14w05a": "https://piston-data.mojang.com/v1/objects/27abecb729cab3a6e11f635dae2cf9be5f620a75/server.jar",
    "14w05b": "https://piston-data.mojang.com/v1/objects/d2d2b00952748af9ee8e60f49b9998dcfad3071f/server.jar",
    "14w06a": "https://piston-data.mojang.com/v1/objects/a6a41979ed198086f2c8ae638f26286b2dc931db/server.jar",
    "14w06b": "https://piston-data.mojang.com/v1/objects/0591a5e7e299182c6849e705704095d2a1efe1d5/server.jar",
    "14w07a": "https://piston-data.mojang.com/v1/objects/de78ac487cf3fb6770e8c15f83e2219d4df851ae/server.jar",
    "14w08a": "https://piston-data.mojang.com/v1/objects/a2716623b9e2c01cf0a1ec44497cc3279fce8f6a/server.jar",
    "14w10a": "https://piston-data.mojang.com/v1/objects/03503dc8c3f615bf8b65d8e1ebbf923e81162e3e/server.jar",
    "14w10b": "https://piston-data.mojang.com/v1/objects/2dd525cb725635b94c763c2efa5e1fe931a0d6d6/server.jar",
    "14w10c": "https://piston-data.mojang.com/v1/objects/d97cc24dad232b5452644facde54c47854283b99/server.jar",
    "1.7.6-pre1": "https://piston-data.mojang.com/v1/objects/121176f19f38780d0cd04bef87c1296fedb37cd0/server.jar",
    "1.7.6-pre2": "https://piston-data.mojang.com/v1/objects/5aa5deddbe750a384bdb5ed0652bbda33cf4e5c8/server.jar",
    "14w11a": "https://piston-data.mojang.com/v1/objects/286924e7082ff1f6baed77a100f73abae81f25e3/server.jar",
    "14w11b": "https://piston-data.mojang.com/v1/objects/58694879e09c500dccb00751ed85a1d6b983229d/server.jar",
    "14w17a": "https://piston-data.mojang.com/v1/objects/701dca9511fa3e6b26799d11475fb3a719d6a26a/server.jar",
    "14w18a": "https://piston-data.mojang.com/v1/objects/48d6b3b47e870f61a95645e2bc1a84a27a1da068/server.jar",
    "14w18b": "https://piston-data.mojang.com/v1/objects/d7300a576860c056938760153cbf56ed98e9c7f9/server.jar",
    "14w19a": "https://piston-data.mojang.com/v1/objects/a7df79e00c4d75e3916438658839785a476bd6ac/server.jar",
    "1.7.10-pre1": "https://piston-data.mojang.com/v1/objects/db79ef4be8b37093c7ca4ddbd54ede2ca21d2a9f/server.jar",
    "1.7.10-pre2": "https://piston-data.mojang.com/v1/objects/ea9fdacf5b0eadfbec5f8aed89c4da3c6be87060/server.jar",
    "1.7.10-pre3": "https://piston-data.mojang.com/v1/objects/b9fdcbd17407d9eaeedcf4ff79b3121ee40133db/server.jar",
    "1.7.10-pre4": "https://piston-data.mojang.com/v1/objects/7c8249c626996c4474afe4f26071a91e7efd825a/server.jar",
    "14w20a": "https://piston-data.mojang.com/v1/objects/4dfd82a84113cfb7e4b489c52caa68bc3f21198e/server.jar",
    "14w20b": "https://piston-data.mojang.com/v1/objects/93ff3d1043ecf25eaf7c9626d8cbde7986dde65d/server.jar",
    "14w21a": "https://piston-data.mojang.com/v1/objects/7e26d5c2feb9df58353b942418640164a8cd0fbd/server.jar",
    "14w21b": "https://piston-data.mojang.com/v1/objects/b02c5506df94aa5d5200ef063f1bab22ce260c8a/server.jar",
    "14w25a": "https://piston-data.mojang.com/v1/objects/e22dedab430bc1c0f938a1e1a2811d11fe29f67e/server.jar",
    "14w25b": "https://piston-data.mojang.com/v1/objects/29209a8e73b6f4afa691d0682aa848c2a1f52dd7/server.jar",
    "14w26a": "https://piston-data.mojang.com/v1/objects/9d167e0b009b99d637ad102a1cb4f5aeb1501e45/server.jar",
    "14w26b": "https://piston-data.mojang.com/v1/objects/0b461d7af1194a192f5b7a9a8989bab83f7317b0/server.jar",
    "14w26c": "https://piston-data.mojang.com/v1/objects/247352905e446c66db85ecb26361a9b5a8eec4ea/server.jar",
    "14w27a": "https://piston-data.mojang.com/v1/objects/b5350953ff062646d4a61b7c8fb4c0570829843a/server.jar",
    "14w27b": "https://piston-data.mojang.com/v1/objects/c5be337237224f752b2ea09d3a2a00a00b26e14b/server.jar",
    "14w28a": "https://piston-data.mojang.com/v1/objects/6987a36f248e88fd8b2366e87fd88834b4a06f7a/server.jar",
    "14w28b": "https://piston-data.mojang.com/v1/objects/aacec09f5ed0475eb474052a4a55b3ca6edaeecc/server.jar",
    "14w29a": "https://piston-data.mojang.com/v1/objects/c16a61be653b5921391c55b337640ddfd7a5b472/server.jar",
    "14w29b": "https://piston-data.mojang.com/v1/objects/b81bb5f919d5489859e9a38c7f6b49e6931a8cc8/server.jar",
    "14w30a": "https://piston-data.mojang.com/v1/objects/cb7bd4bebcb40c128a571c8f15fe1990b1f50a32/server.jar",
    "14w30b": "https://piston-data.mojang.com/v1/objects/ee24a6e63b007b9ec97a591afe1a29a6bbbfe143/server.jar",
    "14w30c": "https://piston-data.mojang.com/v1/objects/2c936d1f410d636a348f100ab926d94d92b743b7/server.jar",
    "14w31a": "https://piston-data.mojang.com/v1/objects/05fde0b4039104a27df8c7b95d327ecafc06cde7/server.jar",
    "14w32a": "https://piston-data.mojang.com/v1/objects/d3b96be87d921fa4f95ea43e5283a253b778f24e/server.jar",
    "14w32b": "https://piston-data.mojang.com/v1/objects/8aa6b045d31cc4a9224ecce602e9f5f748d8f460/server.jar",
    "14w32c": "https://piston-data.mojang.com/v1/objects/5fee0612322feaf374867336375810580da6fab9/server.jar",
    "14w32d": "https://piston-data.mojang.com/v1/objects/83d7acb6f94dc606591ebe4d7a06ad29127cd3de/server.jar",
    "14w33a": "https://piston-data.mojang.com/v1/objects/6c0d06c1b3d8c3365be6e1b9b269725eb4e05ee7/server.jar",
    "14w33b": "https://piston-data.mojang.com/v1/objects/7e0e5511b0049ba92e5c991b6bd0264932559af2/server.jar",
    "14w33c": "https://piston-data.mojang.com/v1/objects/5479bbd5f4717d7c8bc8ca895b3e0894e490814e/server.jar",
    "14w34a": "https://piston-data.mojang.com/v1/objects/e59eecd2f79579f7b87a89b14aa07671eb94c9b1/server.jar",
    "14w34b": "https://piston-data.mojang.com/v1/objects/7991f32cd598ac7e5a8cf11d91965e597ae148b6/server.jar",
    "14w34c": "https://piston-data.mojang.com/v1/objects/5ab3e11d059a6f321a1d284d6849b95264d77e66/server.jar",
    "14w34d": "https://piston-data.mojang.com/v1/objects/0e05b086df677d9802ff5335719149ea90b6f302/server.jar",
    "1.8-pre1": "https://piston-data.mojang.com/v1/objects/88b759849519ca8a7592a2e90d6891c98f50cc17/server.jar",
    "1.8-pre2": "https://piston-data.mojang.com/v1/objects/5673d722ac14f571e6a46f368d34b144e90ef8ad/server.jar",
    "1.8-pre3": "https://piston-data.mojang.com/v1/objects/27fb956fd88ab39205c7c45a39ca4e8820f96cc4/server.jar",
    "1.8.1-pre1": "https://piston-data.mojang.com/v1/objects/dae8203bc40eb43e15e6e9ed454404f330c591f2/server.jar",
    "1.8.1-pre2": "https://piston-data.mojang.com/v1/objects/d0b163d9a442e8b49187e4925ef75970ad451f41/server.jar",
    "1.8,1-pre3": "https://piston-data.mojang.com/v1/objects/22440c0335d95efb7d52d9c844108aa2c69da179/server.jar",
    "1.8.1-pre4": "https://piston-data.mojang.com/v1/objects/5420c131b360f58ecbeb970127a49b525b28f921/server.jar",
    "1.8.1-pre5": "https://piston-data.mojang.com/v1/objects/a25350da18085ab12f01ba56ab03c562cc722a40/server.jar",
    "1.8.2-pre1": "https://piston-data.mojang.com/v1/objects/32320f5d6162cceed3cf618f3c37bde6978eacf2/server.jar",
    "1.8.2-pre2": "https://piston-data.mojang.com/v1/objects/4c32f01c356568b6c6b3cecf4ab4d0f0e7e14fab/server.jar",
    "1.8.2-pre3": "https://piston-data.mojang.com/v1/objects/dd98a2d8148cdaa92fc0deb4201186d552201314/server.jar",
    "1.8.2-pre4": "https://piston-data.mojang.com/v1/objects/b1d4937d5c39c5e1c462d39cc081544170c962b3/server.jar",
    "1.8.2-pre5": "https://piston-data.mojang.com/v1/objects/0226544b417d842a3a78797784615f11f1262a79/server.jar",
    "1.8.2-pre6": "https://piston-data.mojang.com/v1/objects/cc40241ef5acc247048b9d351aefa6288de13d8b/server.jar",
    "1.8.2-pre7": "https://piston-data.mojang.com/v1/objects/61039f9df585c52fbeb2e95d1754852ac00b4344/server.jar",
    "15w31a": "https://piston-data.mojang.com/v1/objects/7799f1f6a486be08185b470a64ca4649e37de578/server.jar",
    "15w31b": "https://piston-data.mojang.com/v1/objects/67f5af98eeef5f6267aca782ea3a536d50f33bc6/server.jar",
    "15w31c": "https://piston-data.mojang.com/v1/objects/4fec021cc8110ce87451e22e23e958ce9d8d61f2/server.jar",
    "15w32a": "https://piston-data.mojang.com/v1/objects/5cb1aa4a4b26979405cea5a181bbe38b72a85add/server.jar",
    "15w32b": "https://piston-data.mojang.com/v1/objects/53c13fc634c89d408155553ebc8724f4b900fa1f/server.jar",
    "15w32c": "https://piston-data.mojang.com/v1/objects/6bef1fd3f1cb34b1d6654d93c43abb899072bd24/server.jar",
    "15w33a": "https://piston-data.mojang.com/v1/objects/b2f50a0daf6fd2e70dac4d7da302524566b57a55/server.jar",
    "15w33b": "https://piston-data.mojang.com/v1/objects/991c628d7c3ea224d90539297d8c2e9127b2489f/server.jar",
    "15w33c": "https://piston-data.mojang.com/v1/objects/042b351243f4236d02976ffc1e7f83f93ac932c7/server.jar",
    "15w34a": "https://piston-data.mojang.com/v1/objects/70103317cd7b973e4f8511a5d8973da20c6654d1/server.jar",
    "15w34b": "https://piston-data.mojang.com/v1/objects/6ee63157f9201f461e056652831348b9c1a51d8c/server.jar",
    "15w34c": "https://piston-data.mojang.com/v1/objects/639946a883a6a2636a82641a1fe4c9243c8e633c/server.jar",
    "15w34d": "https://piston-data.mojang.com/v1/objects/8bf058527fd4bd5d2951e1573d0ff849aedb0197/server.jar",
    "15w35a": "https://piston-data.mojang.com/v1/objects/a3a1c19d861bce39a129ef18226449ea02afb58a/server.jar",
    "15w35b": "https://piston-data.mojang.com/v1/objects/e92badd361f83730436c010044099fdf1af60bab/server.jar",
    "15w35c": "https://piston-data.mojang.com/v1/objects/a0f20e4bdd79e53d923d3fe2853ba11da993e6a1/server.jar",
    "15w35d": "https://piston-data.mojang.com/v1/objects/ed244d36678d875b979f81dbea05acacb89dc4d1/server.jar",
    "15w35e": "https://piston-data.mojang.com/v1/objects/04ade8521778da7786ea9c8bbda2fac005229e0f/server.jar",
    "15w36a": "https://piston-data.mojang.com/v1/objects/ee0b49a2fff99c93b7a216931c11292537eed473/server.jar",
    "15w36b": "https://piston-data.mojang.com/v1/objects/81ab225579322b61b3a37f7d56f400077c1c5978/server.jar",
    "15w36c": "https://piston-data.mojang.com/v1/objects/72a23cbf5f21b3589e230164f5c40c1aa7de36cd/server.jar",
    "15w36d": "https://piston-data.mojang.com/v1/objects/b862ed48ecf134683470145662ac8cb0e1ca7e4d/server.jar",
    "15w37a": "https://piston-data.mojang.com/v1/objects/0f29d64f94ccc40d01ebc1ddd0c506edca7b5dfb/server.jar",
    "15w38a": "https://piston-data.mojang.com/v1/objects/9b14cce8545a6f03f16ef52ef8a2725afaea5c1c/server.jar",
    "15w38b": "https://piston-data.mojang.com/v1/objects/41f8ae90397575214b958bb5ef99d25b541fe366/server.jar",
    "15w39a": "https://piston-data.mojang.com/v1/objects/871b86fac1a4d71642166e0deba2a4b85780d82a/server.jar",
    "15w39b": "https://piston-data.mojang.com/v1/objects/031a5a79a1548f54c7bd148f6f3cf9e42fbd3222/server.jar",
    "15w39c": "https://piston-data.mojang.com/v1/objects/d3f7fb05eef0331941b4161b1f2f2ded7151bbaf/server.jar",
    "15w40a": "https://piston-data.mojang.com/v1/objects/d3f7fb05eef0331941b4161b1f2f2ded7151bbaf/server.jar",
    "15w40b": "https://piston-data.mojang.com/v1/objects/adba98d3a02da95106d782991a90a199d38e5d9f/server.jar",
    "15w41a": "https://piston-data.mojang.com/v1/objects/92fcc884b954fb7e87b163d478fd5ff91bdb1550/server.jar",
    "15w41b": "https://piston-data.mojang.com/v1/objects/994a048f6a3f8f800f2807545b8401617c553dfc/server.jar",
    "15w42a": "https://piston-data.mojang.com/v1/objects/d789ab5179e3bb5d298d82570ee123457cfdfb94/server.jar",
    "15w43a": "https://piston-data.mojang.com/v1/objects/dfc6b233c097fa377f35972e7c95e3c23c632f3c/server.jar",
    "15w43b": "https://piston-data.mojang.com/v1/objects/3154e2f53b1a50159d53f0dc8e4f47857344690f/server.jar",
    "15w43c": "https://piston-data.mojang.com/v1/objects/e514e7107639d2e8b285ceff5eaa114379dafba7/server.jar",
    "15w44a": "https://piston-data.mojang.com/v1/objects/087cd273ee072bf626f89da4ccbb2841854f39ed/server.jar",
    "15w44b": "https://piston-data.mojang.com/v1/objects/7bda3375d5509536766d65cf47b2a17ef42b964a/server.jar",
    "15w45a": "https://piston-data.mojang.com/v1/objects/6bae28a2f80749ba7fc379e44acc46ac5fe44920/server.jar",
    "15w46a": "https://piston-data.mojang.com/v1/objects/f0f25f22430b0c122308244f210df66ae3ce7894/server.jar",
    "15w47a": "https://piston-data.mojang.com/v1/objects/2299e712df1aacb7297d63b75a5299fe35c9b9fd/server.jar",
    "15w47b": "https://piston-data.mojang.com/v1/objects/80cfe2c26ef21e10feb1458c46c244caa07ebcf1/server.jar",
    "15w47c": "https://piston-data.mojang.com/v1/objects/9ec245a239150ccb0f8cdae430d25ed04899bb51/server.jar",
    "15w49a": "https://piston-data.mojang.com/v1/objects/63e4904766e1af15c1a4a412ec3aeb9c5972176d/server.jar",
    "15w49b": "https://piston-data.mojang.com/v1/objects/e376081a73fe429c23db41a99a68a4b04c53ba8e/server.jar",
    "15w50a": "https://piston-data.mojang.com/v1/objects/3ce8624859c8d38b38d2209e30f4fe76b2866de9/server.jar",
    "15w51a": "https://piston-data.mojang.com/v1/objects/4d5f4d2111272d67f2238b83a552599b9b7ad92f/server.jar",
    "15w51b": "https://piston-data.mojang.com/v1/objects/4d5f4d2111272d67f2238b83a552599b9b7ad92f/server.jar",
    "16w02a": "https://piston-data.mojang.com/v1/objects/c574c54826489e1c04dd54d634da83945824337b/server.jar",
    "16w03a": "https://piston-data.mojang.com/v1/objects/c574c54826489e1c04dd54d634da83945824337b/server.jar",
    "16w04a": "https://piston-data.mojang.com/v1/objects/8b7d974f3161ddb90b14ff77a668bf0350689bb2/server.jar",
    "16w05a": "https://piston-data.mojang.com/v1/objects/d74a9989d7dcd73c90191a65ae09e15b2371ffbd/server.jar",
    "16w05b": "https://piston-data.mojang.com/v1/objects/9fdf8a90055b3cf689265cc30bdd9d1faf2c743c/server.jar",
    "16w06a": "https://piston-data.mojang.com/v1/objects/c4da6936d6374fd7116900135a2ae664de63d3bf/server.jar",
    "16w07a": "https://piston-data.mojang.com/v1/objects/f2bfcb799a616611801ff0295312e563f782ff78/server.jar",
    "16w07b": "https://piston-data.mojang.com/v1/objects/f2bfcb799a616611801ff0295312e563f782ff78/server.jar",
    "1.9-pre1": "https://piston-data.mojang.com/v1/objects/e166c9863dc5a6444d8260b46423325d4130b429/server.jar",
    "1.9-pre2": "https://piston-data.mojang.com/v1/objects/ac6c4226ca5f1f7ea4c6f936f88d1df7c82d3a92/server.jar",
    "1.9-pre3": "https://piston-data.mojang.com/v1/objects/db995628b109fd83953ffadb749c2432fac70d9e/server.jar",
    "1.9-pre4": "https://piston-data.mojang.com/v1/objects/bbcbe9f89ef3cacd96dfd1df4d88588369fbd767/server.jar",
    "1.9.1-pre1": "https://piston-data.mojang.com/v1/objects/04a6ca96d4024050c50570731568b94771ff7910/server.jar",
    "1.9.1-pre2": "https://piston-data.mojang.com/v1/objects/bc7000381cec5819aefeea8b68ecc232208ab3ad/server.jar",
    "1.9.1-pre3": "https://piston-data.mojang.com/v1/objects/6cf7cb1c561e2915c4370bfb4cf3f5e10058d537/server.jar",
    "16w14a": "https://piston-data.mojang.com/v1/objects/5616b2213b727241821a137b4ef290c7bbace20a/server.jar",
    "16w15a": "https://piston-data.mojang.com/v1/objects/c254bc24caac3f6d5059f2cc64a80ded2e164289/server.jar",
    "16w15b": "https://piston-data.mojang.com/v1/objects/5add6bcbd04c20bef6ed5db4431651c0c1282489/server.jar",
    "1.9.3-pre1": "https://piston-data.mojang.com/v1/objects/5d7391b36ccbc4ec04a259a3f7c6609232f30762/server.jar",
    "1.9.3-pre2": "https://piston-data.mojang.com/v1/objects/41c29ba7fca8d2a0ce3bab620600459e6023458c/server.jar",
    "1.9.3-pre3": "https://piston-data.mojang.com/v1/objects/ef902371fa5cbb50288b4801f9e58432c627d8e7/server.jar",
    "16w20a": "https://piston-data.mojang.com/v1/objects/2cbcbd735cb48c8cc2bebb7b43c8afa69a923269/server.jar",
    "16w21a": "https://piston-data.mojang.com/v1/objects/12d65aa459d3e93643746dce14c100b05fbcdddf/server.jar",
    "16w21b": "https://piston-data.mojang.com/v1/objects/6dedac03d0fbfbcabe8ef09b170a577a9f72c6f8/server.jar",
    "1.10-pre1": "https://piston-data.mojang.com/v1/objects/c9c34ba406f694e56c1729b465c25e0f63ce9743/server.jar",
    "1.10-pre2": "https://piston-data.mojang.com/v1/objects/aa4ec0004eb20a70ef7426816cae992d73718038/server.jar",
    "16w32a": "https://piston-data.mojang.com/v1/objects/b1309cff6c574e9487e3413773841ef5eb260587/server.jar",
    "16w32b": "https://piston-data.mojang.com/v1/objects/b912ff1468e93003f36cda32db5d70133b517f97/server.jar",
    "16w33a": "https://piston-data.mojang.com/v1/objects/dfdda3e5ba769ba0634ad43ca1124a401d6addca/server.jar",
    "16w35a": "https://piston-data.mojang.com/v1/objects/16ad43cb3b87b0279028af26201af7651b87c9e0/server.jar",
    "16w36a": "https://piston-data.mojang.com/v1/objects/921580b22ce7d48f9d541364a3b04eebb680222e/server.jar",
    "16w38a": "https://piston-data.mojang.com/v1/objects/95ffd7c33ad9f978d4a23762978923b96fc0aa7e/server.jar",
    "16w39a": "https://piston-data.mojang.com/v1/objects/f5e840e9f37ae7f50c9c979669279bcc68c91fa7/server.jar",
    "16w39b": "https://piston-data.mojang.com/v1/objects/07eb3f85fc848ec8e209377aee1f7f574566e130/server.jar",
    "16w39c": "https://piston-data.mojang.com/v1/objects/df13c6cbf5fc735896b22f56b1f8940dd11a3b5f/server.jar",
    "16w40a": "https://piston-data.mojang.com/v1/objects/64a1a5ba3f347c5e03477b42ac13d10ee193b51c/server.jar",
    "16w41a": "https://piston-data.mojang.com/v1/objects/94f47b24edd154d89240e49d9b7371e74f433d19/server.jar",
    "16w42a": "https://piston-data.mojang.com/v1/objects/ad6aa39daf88864fcd84b231638e3dc28bde83f3/server.jar",
    "16w43a": "https://piston-data.mojang.com/v1/objects/c5cc57bfd0a3462c2634a37c83877e91f25f020b/server.jar",
    "16w44a": "https://piston-data.mojang.com/v1/objects/9f30eff92cc234034581f0a1ef40c6d76f6b3e69/server.jar",
    "1.11-pre1": "https://piston-data.mojang.com/v1/objects/7e2884f11e3fb52ed1ad82376e3cada3aa95152e/server.jar",
    "16w50a": "https://piston-data.mojang.com/v1/objects/d4d30a5433846d205974ace4cf34c9b294e0833f/server.jar",
    "17w06a": "https://piston-data.mojang.com/v1/objects/37441cab126ee2a4f292c9bf488c9dd800cff841/server.jar",
    "17w13a": "https://piston-data.mojang.com/v1/objects/d3806f89b9c90cbfb78919a3bcc010ad2e5d6ebb/server.jar",
    "17w13b": "https://piston-data.mojang.com/v1/objects/7bd51f821ed09b6a1d3a9a9b2fc67b48f1d829c4/server.jar",
    "17w14a": "https://piston-data.mojang.com/v1/objects/0530caf1d099fc730ca335a21bcf2fbb58c42c64/server.jar",
    "17w15a": "https://piston-data.mojang.com/v1/objects/cc26caa34e1a53326ec374d229db07a0e2a7de17/server.jar",
    "17w16a": "https://piston-data.mojang.com/v1/objects/47cfe5d44ccf6333b697da3e82e35bb3725e53d8/server.jar",
    "17w16b": "https://piston-data.mojang.com/v1/objects/80601961e590046727791d6b18f51d840ea86e1c/server.jar",
    "17w17a": "https://piston-data.mojang.com/v1/objects/3795d253cfef44f1f1467422b4399d1770484dc0/server.jar",
    "17w17b": "https://piston-data.mojang.com/v1/objects/7cf669824e4c8340050adcc2125f1ec4cb84feac/server.jar",
    "17w18a": "https://piston-data.mojang.com/v1/objects/b1f45946bd74f4e2cf1833324770809ebcd0b7b1/server.jar",
    "17w18b": "https://piston-data.mojang.com/v1/objects/915c1833209d588ade3e064577700037093861da/server.jar",
    "1.12-pre1": "https://piston-data.mojang.com/v1/objects/ebcafa3e1a3312500893087bf4bfb6c6f335ef0e/server.jar",
    "1.12-pre2": "https://piston-data.mojang.com/v1/objects/e5fd1c4202f9b0855d9104b66ba4182d52e79c38/server.jar",
    "1.12-pre3": "https://piston-data.mojang.com/v1/objects/c985b2083848efcc8d1658d6cda5644681035f80/server.jar",
    "1.12-pre4": "https://piston-data.mojang.com/v1/objects/588bcccfff42acc2cb6f7c6470cd6bc8ba393668/server.jar",
    "1.12-pre5": "https://piston-data.mojang.com/v1/objects/40e76b2836c92cd9e05af61bb64046c8650c088d/server.jar",
    "1.12-pre6": "https://piston-data.mojang.com/v1/objects/9bc0e57debc61da93c0ea0d97849254db4f4e556/server.jar",
    "1.12-pre7": "https://piston-data.mojang.com/v1/objects/a8d79598161edc5f67b606120ea9e62bcefcaaa7/server.jar",
    "17w31a": "https://piston-data.mojang.com/v1/objects/00b83b98c91dbe3531342325f72654ef6d7be6eb/server.jar",
    "1.12.1-pre1": "https://piston-data.mojang.com/v1/objects/b25c39f4658911169e184f00a24798f6463ded14/server.jar",
    "1.12.2-pre1": "https://piston-data.mojang.com/v1/objects/b81c81335e68731d66ccddc21df0c06d7b9b46ab/server.jar",
    "1.12.2-pre2": "https://piston-data.mojang.com/v1/objects/641adfb6a646fe12f1fb2715ed4e3167c7ff2f2b/server.jar",
    "17w43a": "https://piston-data.mojang.com/v1/objects/6f6869d527140e5531e655bda10911efb65425bb/server.jar",
    "17w43b": "https://piston-data.mojang.com/v1/objects/0447782ac5280f8f981c3998609928984213a4c7/server.jar",
    "17w45a": "https://piston-data.mojang.com/v1/objects/471b2dfa12e4df234057159ce5ee8320da3c84c1/server.jar",
    "17w45b": "https://piston-data.mojang.com/v1/objects/eec0c6c49b1066b648f39e1dcef8c76510a794dc/server.jar",
    "17w46a": "https://piston-data.mojang.com/v1/objects/9127416e2341eb8fb7b63636c3ae39efefb2843b/server.jar",
    "17w47a": "https://piston-data.mojang.com/v1/objects/0cec7f11d7bf9c36464b1815e5bbcb0afe6db019/server.jar",
    "17w47b": "https://piston-data.mojang.com/v1/objects/9b4e7894906f0b379c7300cff0b3e68a4b9db662/server.jar",
    "17w48a": "https://piston-data.mojang.com/v1/objects/e132a348243b824ba6f74569c8b1080b77104981/server.jar",
    "17w49a": "https://piston-data.mojang.com/v1/objects/561fe37463ef30b4e1ab4c6b1da057d9e2b17801/server.jar",
    "17w49b": "https://piston-data.mojang.com/v1/objects/caac50590085014355070ea6381baec0f58aa9f2/server.jar",
    "17w50a": "https://piston-data.mojang.com/v1/objects/670c67a4dfbd1070a9be629124ddd8aac8d9b9d9/server.jar",
    "18w01a": "https://piston-data.mojang.com/v1/objects/47a8d2bb4db5b5e3db6b7837c9f0fa17ea660448/server.jar",
    "18w02a": "https://piston-data.mojang.com/v1/objects/950b737e9cefc9f91f286190166f062d6b0e0105/server.jar",
    "18w03a": "https://piston-data.mojang.com/v1/objects/713a291a4da5cad056964c1fcda8c888e154eb73/server.jar",
    "18w03b": "https://piston-data.mojang.com/v1/objects/ef8c70a7c9b88c02c64ea01d050614929b7152f6/server.jar",
    "18w05a": "https://piston-data.mojang.com/v1/objects/a4029c808cef57bed3228a51dcb7f68edd018a77/server.jar",
    "18w06a": "https://piston-data.mojang.com/v1/objects/4e47158fd42d966884a7ffb7440b35d86c038049/server.jar",
    "18w07a": "https://piston-data.mojang.com/v1/objects/4e47158fd42d966884a7ffb7440b35d86c038049/server.jar",
    "18w07b": "https://piston-data.mojang.com/v1/objects/669811c0df3fedef8a15f1b31c96df966b9aee79/server.jar",
    "18w07c": "https://piston-data.mojang.com/v1/objects/52e141870c3c850811710f2ba07eb3e7e583ea92/server.jar",
    "18w08a": "https://piston-data.mojang.com/v1/objects/09b2bc558d86878ce69f303ddbd62bf4489db068/server.jar",
    "18w08b": "https://piston-data.mojang.com/v1/objects/cdfdcdd799087d9b66f04667f0717a11e28c29cc/server.jar",
    "18w09a": "https://piston-data.mojang.com/v1/objects/57dd2fe4a2fdb6e846b978e77442465d2ea27f43/server.jar",
    "18w10a": "https://piston-data.mojang.com/v1/objects/7bb1cfb4560d2e99551b22a631b6087d43817a45/server.jar",
    "18w10b": "https://piston-data.mojang.com/v1/objects/b45d7194b91327c8fd2c1d0d5a738b80c9600562/server.jar",
    "18w10c": "https://piston-data.mojang.com/v1/objects/7c2494311ab74f97623ebf6e2d5beba625a9d5fc/server.jar",
    "18w10d": "https://piston-data.mojang.com/v1/objects/28727c7dfb62c56ac48153ab9a25d42115f85f94/server.jar",
    "18w11a": "https://piston-data.mojang.com/v1/objects/4286b7cbc4709c8f61c93a77b42c70918376cac3/server.jar",
    "18w14a": "https://piston-data.mojang.com/v1/objects/50b4ca8fe7853ae6757a163a80e67cb8437fb082/server.jar",
    "18w14b": "https://piston-data.mojang.com/v1/objects/85d6445fc4596e6b69fb00f0d3e5462dfeeb933c/server.jar",
    "18w15a": "https://piston-data.mojang.com/v1/objects/3f9534ab77a524593db7a20196e41ae36b23d69d/server.jar",
    "18w16a": "https://piston-data.mojang.com/v1/objects/3f9534ab77a524593db7a20196e41ae36b23d69d/server.jar",
    "18w19a": "https://piston-data.mojang.com/v1/objects/97ad982d57fb7b7cb9dc28ffd87c79538b1901f6/server.jar",
    "18w19b": "https://piston-data.mojang.com/v1/objects/87edb914af0594016fab77eaaa9d25c7f1f1d132/server.jar",
    "18w20a": "https://piston-data.mojang.com/v1/objects/108a051216637e0145f6b0e66182b48736595fc3/server.jar",
    "18w20b": "https://piston-data.mojang.com/v1/objects/35304e17de5fbe503b10bad50192d14a38e5cec0/server.jar",
    "18w20c": "https://piston-data.mojang.com/v1/objects/9e0ffb265e3771dc5c7b56f291b9c9d8f668f48b/server.jar",
    "18w21a": "https://piston-data.mojang.com/v1/objects/2022a23da58dc55371b6a182fb1ba59742dc66a2/server.jar",
    "18w21b": "https://piston-data.mojang.com/v1/objects/df8cc7cfa4c2d24f31f5997a102f1d6411f038d0/server.jar",
    "18w22a": "https://piston-data.mojang.com/v1/objects/077225ee7bca03f521ed8df86fa4740b8e7a3cad/server.jar",
    "18w22b": "https://piston-data.mojang.com/v1/objects/cc0b6a96e537528cdaab685c4eaeeaf8ed905b51/server.jar",
    "18w22c": "https://piston-data.mojang.com/v1/objects/d66173b86e26e6835e36c63eb2828652186a4698/server.jar",
    "1.13-pre1": "https://piston-data.mojang.com/v1/objects/e031e58e1d9e745877404530d39775bf9ffa9a56/server.jar",
    "1.13-pre2": "https://piston-data.mojang.com/v1/objects/5b312060d457a1f75846afd3935ec3f140da3942/server.jar",
    "1.13-pre3": "https://piston-data.mojang.com/v1/objects/5406f31cb5274ae48938851de697b32976ecb499/server.jar",
    "1.13-pre4": "https://piston-data.mojang.com/v1/objects/d57007a8722ed645319666fc56b27690054d8363/server.jar",
    "1.13-pre5": "https://piston-data.mojang.com/v1/objects/6d9ede222df5726059aba1b01f99c328bc16f1a5/server.jar",
    "1.13-pre6": "https://piston-data.mojang.com/v1/objects/71a2f9a760f0cbcf09d1eae60eebe1ccbb7ea1db/server.jar",
    "1.13-pre7": "https://piston-data.mojang.com/v1/objects/6cd8348fadedaa1de5851f449b995c835bb569eb/server.jar",
    "1.13-pre8": "https://piston-data.mojang.com/v1/objects/b04f82ae0f3018c4c22a153184b385012c4d0814/server.jar",
    "1.13-pre9": "https://piston-data.mojang.com/v1/objects/ee66f5cb1247f4340734a151db4f940bbe04f833/server.jar",
    "1.13-pre10": "https://piston-data.mojang.com/v1/objects/2ffcae7a9489d515b0f733430923ef974dffd56b/server.jar",
    "18w30a": "https://piston-data.mojang.com/v1/objects/4cfe675115064caad14712c3345660f4069a2e8b/server.jar",
    "18w30b": "https://piston-data.mojang.com/v1/objects/373b2fb24db8ed21d25483a986e9eb7f945c5277/server.jar",
    "18w31a": "https://piston-data.mojang.com/v1/objects/4646084899fb62a7b9afa6f453fae4e6e786e5a5/server.jar",
    "18w32a": "https://piston-data.mojang.com/v1/objects/d36429ccdcaa73cb37b366d608024e3a6a5a20ab/server.jar",
    "18w33a": "https://piston-data.mojang.com/v1/objects/e62f0a29e4ab5963488330f29c03ca2914b5b22b/server.jar",
    "1.13.1-pre1": "https://piston-data.mojang.com/v1/objects/988fec4e71e5fa1fc29a50230de05a11973d62ab/server.jar",
    "1.13.1-pre2": "https://piston-data.mojang.com/v1/objects/c2a4bcf3e244c46f13c39e31e7ef6030564fb6c2/server.jar",
    "1.13.2-pre1": "https://piston-data.mojang.com/v1/objects/744df5d6872645a8f919459473e0e02a3571e6bb/server.jar",
    "1.13.2-pre2": "https://piston-data.mojang.com/v1/objects/2f39df32f20196b5a6acad117f7d6b404b069c58/server.jar",
    "18w43a": "https://piston-data.mojang.com/v1/objects/08ca3aaa7ff61d4ae06d5d63476724a1f32cb6b0/server.jar",
    "18w43b": "https://piston-data.mojang.com/v1/objects/ed443be5ff6a304164612c545f0942fd99d53e13/server.jar",
    "18w43c": "https://piston-data.mojang.com/v1/objects/b2dc0522b0802cbb8e81d1afd3e46be8819d3c1d/server.jar",
    "18w44a": "https://piston-data.mojang.com/v1/objects/e70221701d85ad9ed8be35e042f4c8e52fb627ec/server.jar",
    "18w45a": "https://piston-data.mojang.com/v1/objects/a004069d93ebfd9a6d93c57b66becac29f876d4c/server.jar",
    "18w46a": "https://piston-data.mojang.com/v1/objects/6681e24d2dc9ba60a6e7d1fbbf25b2af70ff9d1c/server.jar",
    "18w47a": "https://piston-data.mojang.com/v1/objects/7066873e9b86cfcd5b66c6a98d2587d95bf94adc/server.jar",
    "18w47b": "https://piston-data.mojang.com/v1/objects/fa9d22eea98b62f6663f1aa8a25840e0993485e6/server.jar",
    "18w48a": "https://piston-data.mojang.com/v1/objects/f0f04983d197388b05a4647f7a7cf8b5fbbac5d3/server.jar",
    "18w48b": "https://piston-data.mojang.com/v1/objects/cfa41132beeb877a093e044aba591d9dae236c38/server.jar",
    "18w49a": "https://piston-data.mojang.com/v1/objects/5b6eb767f6708d351e3d1009a44115bb033b854f/server.jar",
    "18w50a": "https://piston-data.mojang.com/v1/objects/de0577900a9071758d7f1172dd283bdbe88b7431/server.jar",
    "19w02a": "https://piston-data.mojang.com/v1/objects/f8078dd487483a917645f7a5561290e28bd875c4/server.jar",
    "19w03a": "https://piston-data.mojang.com/v1/objects/1e80738a5360887bc93a46bdffb07699a45bf5a1/server.jar",
    "19w03b": "https://piston-data.mojang.com/v1/objects/a3a358a7566debb17c5332fbc43eb8b84e000997/server.jar",
    "19w03c": "https://piston-data.mojang.com/v1/objects/e9fdb18631fc4ff23b06b1e827fb653ac20532fe/server.jar",
    "19w04a": "https://piston-data.mojang.com/v1/objects/261edfd76c32c9f675c12264b6fa03f670c3325c/server.jar",
    "19w04b": "https://piston-data.mojang.com/v1/objects/7a5a3bbefcb4d27fd9ac30736eee06ae1e2c0991/server.jar",
    "19w05a": "https://piston-data.mojang.com/v1/objects/521021450baf9b9b98b0a6d0cb60e97f306f4f57/server.jar",
    "19w06a": "https://piston-data.mojang.com/v1/objects/20c069d373e77265aaeeedb733f7051e294325a3/server.jar",
    "19w07a": "https://piston-data.mojang.com/v1/objects/d370db01d591576477c3efc940a42926f43bc98f/server.jar",
    "19w08a": "https://piston-data.mojang.com/v1/objects/f337f8dfb765f152388d5038a6e0e8830782e5ed/server.jar",
    "19w08b": "https://piston-data.mojang.com/v1/objects/f337f8dfb765f152388d5038a6e0e8830782e5ed/server.jar",
    "19w09a": "https://piston-data.mojang.com/v1/objects/266d772f79eebe55de3856ae3fe675c0699cd1ca/server.jar",
    "19w11a": "https://piston-data.mojang.com/v1/objects/388221ffa9e8e1576e07f9839eadd2ac7bd51cbb/server.jar",
    "19w11b": "https://piston-data.mojang.com/v1/objects/1c453ba8ccaabc38d924e7c11fe73c65a1978a33/server.jar",
    "19w12a": "https://piston-data.mojang.com/v1/objects/dc1a1dfef026d38dfc04b360653172f5428f86ef/server.jar",
    "19w12b": "https://piston-data.mojang.com/v1/objects/37d6d9753b8eac2420e9deba132c38e00c8204c3/server.jar",
    "19w13a": "https://piston-data.mojang.com/v1/objects/c63080e9349640fda5820bbe48cacc623c99c496/server.jar",
    "19w13b": "https://piston-data.mojang.com/v1/objects/6d395392d8aac9bcde96322831042c77410b0a19/server.jar",
    "19w14a": "https://piston-data.mojang.com/v1/objects/a786a10223f5218967bfd42a06f4bee9e9563f56/server.jar",
    "19w14b": "https://piston-data.mojang.com/v1/objects/719781c28dbcf7d0576e81fe5e77d75c1f18117f/server.jar",
    "1.14 Pre-Release 1": "https://piston-data.mojang.com/v1/objects/6f27430bcd9b06d3dcb5d2966c75d5e491915c9c/server.jar",
    "1.14 Pre-Release 2": "https://piston-data.mojang.com/v1/objects/353cc74b9aefd4675730449f50f5c0066063ac3f/server.jar",
    "1.14 Pre-Release 3": "https://piston-data.mojang.com/v1/objects/6b747e1338e1aa058146032a659cf654c446552d/server.jar",
    "1.14 Pre-Release 4": "https://piston-data.mojang.com/v1/objects/cf967a23b452ab474bf7bcb69fd029a5f8b84bba/server.jar",
    "1.14 Pre-Release 5": "https://piston-data.mojang.com/v1/objects/5d550762b9c82ab4fe9f259c14fcf7bf7ed8017a/server.jar",
    "1.14.1 Pre-Release 1": "https://piston-data.mojang.com/v1/objects/0bbed1aa2ef4bd4c0d6134461ac3e8eba1dc5f62/server.jar",
    "1.14.1 Pre-Release 2": "https://piston-data.mojang.com/v1/objects/ea3a8bee27e1ca4185bf703fb4e414800f533fc9/server.jar",
    "1.14.2 Pre-Release 1": "https://piston-data.mojang.com/v1/objects/1aad89bfe7a14bee70de0b07339a2f319771180f/server.jar",
    "1.14.2 Pre-Release 2": "https://piston-data.mojang.com/v1/objects/a2cedc73237e999a5d408ecf0923a130d69d45a1/server.jar",
    "1.14.2 Pre-Release 3": "https://piston-data.mojang.com/v1/objects/307fb7e6208bd843060b1844857dc5e1d555a1df/server.jar",
    "1.14.2 Pre-Release 4": "https://piston-data.mojang.com/v1/objects/6bba54ad86fccc45cc68ba410e738d3b331cdadd/server.jar",
    "1.14.3-pre1": "https://piston-data.mojang.com/v1/objects/966984c5d8b5c3604a8838f8fb5635b8b9cd73c7/server.jar",
    "1.14.3-pre2": "https://piston-data.mojang.com/v1/objects/64caea4b63611111d775e4558341cb9718a6ff4f/server.jar",
    "1.14.3-pre3": "https://piston-data.mojang.com/v1/objects/a46e49e1541cf24a75aabe2756514565de83634a/server.jar",
    "1.14.3-pre4": "https://piston-data.mojang.com/v1/objects/d5397db937499277165abb27f8af04885be8b6b6/server.jar",
    "1.14.4-pre1": "https://piston-data.mojang.com/v1/objects/774c5619679673ec772b0f01f363d0145a9d6b51/server.jar",
    "1.14.4-pre2": "https://piston-data.mojang.com/v1/objects/a7023b92091ca5872d35b17c8aab1c6daa833a69/server.jar",
    "1.14.4-pre3": "https://piston-data.mojang.com/v1/objects/b7ed47d4e600c6ead80f4c73c2e080625d07ef6e/server.jar",
    "1.14.4-pre4": "https://piston-data.mojang.com/v1/objects/853bf851bda5862b7f68baf93ae86fb90571ceca/server.jar",
    "1.14.4-pre5": "https://piston-data.mojang.com/v1/objects/f45379dfa2ecd946a2ed81c354225a4181261333/server.jar",
    "1.14.4-pre6": "https://piston-data.mojang.com/v1/objects/d7b8f310278a5ea9efef03b4e441f12524253c5d/server.jar",
    "1.14.4-pre7": "https://piston-data.mojang.com/v1/objects/98d1396495562dbb32828ef50bad7112c403c47e/server.jar",
    "19w34a": "https://piston-data.mojang.com/v1/objects/288962c67d083e35d4313cf0eba8ad1e27173d17/server.jar",
    "19w35a": "https://piston-data.mojang.com/v1/objects/e0bfc54b4b424c43b1fe5b833d68e35d031a481d/server.jar",
    "19w36a": "https://piston-data.mojang.com/v1/objects/c042fd138ae280b01ce191937ca917666a15be38/server.jar",
    "19w37a": "https://piston-data.mojang.com/v1/objects/e2c6923d9e06f6b98460f0f584567848a70bf71b/server.jar",
    "19w38a": "https://piston-data.mojang.com/v1/objects/e40184002fa2e183de5fda0229d0709cfd6bfe8a/server.jar",
    "19w38b": "https://piston-data.mojang.com/v1/objects/aff9049db1bcbd44d133ebfbd015dce49dd8383e/server.jar",
    "19w39a": "https://piston-data.mojang.com/v1/objects/aff9049db1bcbd44d133ebfbd015dce49dd8383e/server.jar",
    "19w40a": "https://piston-data.mojang.com/v1/objects/aff9049db1bcbd44d133ebfbd015dce49dd8383e/server.jar",
    "19w41a": "https://piston-data.mojang.com/v1/objects/aff9049db1bcbd44d133ebfbd015dce49dd8383e/server.jar",
    "19w42a": "https://piston-data.mojang.com/v1/objects/1f8673dee28ff3a1714e17780f6b91d5372fe440/server.jar",
    "19w44a": "https://piston-data.mojang.com/v1/objects/0a68a89351325fbad9b432b3eb24ae944860350e/server.jar",
    "19w45a": "https://piston-data.mojang.com/v1/objects/fa9e744ee6e5cccd4000e2269f8dff8ce96ce5a9/server.jar",
    "19w45b": "https://piston-data.mojang.com/v1/objects/fa9e744ee6e5cccd4000e2269f8dff8ce96ce5a9/server.jar",
    "19w46a": "https://piston-data.mojang.com/v1/objects/3544354ee91fee0439009e71c8e064ec8355600a/server.jar",
    "19w46b": "https://piston-data.mojang.com/v1/objects/eded6ea3899b67478780576a3b92c6cac867b501/server.jar",
    "1.15-pre1": "https://piston-data.mojang.com/v1/objects/332b3382108e5bdb0b23717082c9b97c54ffc8ad/server.jar",
    "1.15-pre2": "https://piston-data.mojang.com/v1/objects/0f0c2e3c25693189374c8a63179e3018ebfdc1ba/server.jar",
    "1.15-pre3": "https://piston-data.mojang.com/v1/objects/eedb663e70f49a5592b88197ea68b0f32fd9ce97/server.jar",
    "1.15-pre4": "https://piston-data.mojang.com/v1/objects/8f9e23414a01d21e2cd313b2595b164ccfda56aa/server.jar",
    "1.15-pre5": "https://piston-data.mojang.com/v1/objects/8f9e23414a01d21e2cd313b2595b164ccfda56aa/server.jar",
    "1.15-pre6": "https://piston-data.mojang.com/v1/objects/8d5793fe302feb6c03d3c5e590ef940fc02f2864/server.jar",
    "1.15-pre7": "https://piston-data.mojang.com/v1/objects/8d5793fe302feb6c03d3c5e590ef940fc02f2864/server.jar",
    "1.15.1-pre1": "https://piston-data.mojang.com/v1/objects/289a247dd42928880769398b049d3890513f2917/server.jar",
    "1.15.2-pre1": "https://piston-data.mojang.com/v1/objects/5db50a719dc40d63aa95c6bdc5b302e425f673f2/server.jar",
    "1.15.2-pre2": "https://piston-data.mojang.com/v1/objects/f3eae938f3382ffeb8c3af150664d33864561110/server.jar",
    "20w06a": "https://piston-data.mojang.com/v1/objects/9b74998642553efe0e4d1aa079dc737b3e4cdc13/server.jar",
    "20w07a": "https://piston-data.mojang.com/v1/objects/3944965e1621a5ccbe99292479cc62e07bccd611/server.jar",
    "20w08a": "https://piston-data.mojang.com/v1/objects/b46203f7cc23ec786710fdcf6f369935cf92dabb/server.jar",
    "20w09a": "https://piston-data.mojang.com/v1/objects/6f1e5ae00b938bbe15560b7174be7a3b4c78c450/server.jar",
    "20w10a": "https://piston-data.mojang.com/v1/objects/6f1e5ae00b938bbe15560b7174be7a3b4c78c450/server.jar",
    "20w11a": "https://piston-data.mojang.com/v1/objects/6f1e5ae00b938bbe15560b7174be7a3b4c78c450/server.jar",
    "20w12a": "https://piston-data.mojang.com/v1/objects/3d9657a172415a163e25096942f5a4d110b984a0/server.jar",
    "20w13a": "https://piston-data.mojang.com/v1/objects/16f18c21286a3f566d3d0431d13aa133bebe6eff/server.jar",
    "20w13b": "https://piston-data.mojang.com/v1/objects/0e00cff8df2532a1ae252e773552c2fd6c68de80/server.jar",
    "20w14a": "https://piston-data.mojang.com/v1/objects/affcf966ca903156070aa90b63417793a78b2165/server.jar",
    "20w15a": "https://piston-data.mojang.com/v1/objects/64ca02e1e9fc7e60eac4aba788580b16eb12f71f/server.jar",
    "20w16a": "https://piston-data.mojang.com/v1/objects/754bbd654d8e6bd90cd7a1464a9e68a0624505dd/server.jar",
    "20w17a": "https://piston-data.mojang.com/v1/objects/0b7e36b084577fb26148c6341d590ac14606db21/server.jar",
    "20w18a": "https://piston-data.mojang.com/v1/objects/4d84832bdc7f62aa96b0d5d5a73b1272e8c474b5/server.jar",
    "20w19a": "https://piston-data.mojang.com/v1/objects/fbb3ad3e7b25e78723434434077995855141ff07/server.jar",
    "20w20a": "https://piston-data.mojang.com/v1/objects/f06a943eb107494688b4447b97514af6d7311623/server.jar",
    "20w20b": "https://piston-data.mojang.com/v1/objects/0393774fb1f9db8288a56dbbcf45022b71f7939f/server.jar",
    "20w21a": "https://piston-data.mojang.com/v1/objects/03b8fa357937d0bdb6650ec8cc74506ec2fd91a7/server.jar",
    "20w22a": "https://piston-data.mojang.com/v1/objects/c4a62eb36917aaa06dc8e20a2a35264d5fda123b/server.jar",
    "1.16-pre1": "https://piston-data.mojang.com/v1/objects/c4a62eb36917aaa06dc8e20a2a35264d5fda123b/server.jar",
    "1.16-pre2": "https://piston-data.mojang.com/v1/objects/8daeb71269eb164097d7d7ab1fa93fc93ab125c3/server.jar",
    "1.16-pre3": "https://piston-data.mojang.com/v1/objects/0b5653b65bc494fa55349682cebf50abf0d72ad9/server.jar",
    "1.16-pre4": "https://piston-data.mojang.com/v1/objects/018cdde89f8ff3831ce27c6c8dbf6831e99e0e75/server.jar",
    "1.16-pre5": "https://piston-data.mojang.com/v1/objects/56081523bca4f7074f111d1e8a9fd0a86d072a2b/server.jar",
    "1.16-pre6": "https://piston-data.mojang.com/v1/objects/8984939f42371a7e614fa48669e308c4cc9ba228/server.jar",
    "1.16-pre7": "https://piston-data.mojang.com/v1/objects/577f7287642309a2a32e80be395329118dfddb3f/server.jar",
    "1.16-pre8": "https://piston-data.mojang.com/v1/objects/d6a747371b200216653be9b4140cd2862eddbb0e/server.jar",
    "1.16-rc1": "https://piston-data.mojang.com/v1/objects/7213e5ba8fe8d352141cf3dde907c26c43480092/server.jar",
    "20w27a": "https://piston-data.mojang.com/v1/objects/40efae0a2412154f44a99f158752b8417b384f06/server.jar",
    "20w28a": "https://piston-data.mojang.com/v1/objects/1e36d315d96c29d8d32aa8fecbfb8efa4243a746/server.jar",
    "20w29a": "https://piston-data.mojang.com/v1/objects/ea9a65a38e000fe76b51fa36e923c09d5d8fa473/server.jar",
    "20w30a": "https://piston-data.mojang.com/v1/objects/ea9a65a38e000fe76b51fa36e923c09d5d8fa473/server.jar",
    "1.16.2-pre1": "https://piston-data.mojang.com/v1/objects/d4434bf4f2f0572a4eb54b3da1b1b3069a4e9ef2/server.jar",
    "1.16.2-pre2": "https://piston-data.mojang.com/v1/objects/d2cae287324631b2b4bfa609dd01c63cd6d4b78d/server.jar",
    "1.16.2-pre3": "https://piston-data.mojang.com/v1/objects/bd47f78f185a525388e446aa44975c147057ebbd/server.jar",
    "1.16.2-rc1": "https://piston-data.mojang.com/v1/objects/203e18d79201b5e8c46019074b07e1c3b4c75f57/server.jar",
    "1.16.2-rc2": "https://piston-data.mojang.com/v1/objects/45287d794fa2631b8da9b9002696ebe406fbed6b/server.jar",
    "1.16.3-rc1": "https://piston-data.mojang.com/v1/objects/562bf3e75afea00875cff4a06165f93056646f32/server.jar",
    "1.16.4-pre1": "https://piston-data.mojang.com/v1/objects/28eb6f8c4c05eec278e3e7f9f0379a16adbfb91d/server.jar",
    "1.16.4-pre2": "https://piston-data.mojang.com/v1/objects/ceb412d94900167f519100736bc5709853b50b8c/server.jar",
    "1.16.4-rc1": "https://piston-data.mojang.com/v1/objects/daf2d997bd6b1725b6d59b48f533a6804d43db33/server.jar",
    "20w45a": "https://piston-data.mojang.com/v1/objects/043ec38297d0ec58abd6f636bc92f5664a8ccecb/server.jar",
    "20w46a": "https://piston-data.mojang.com/v1/objects/373675677cc57b9294a187a4d0ecab6f340d4189/server.jar",
    "20w48a": "https://piston-data.mojang.com/v1/objects/a14d24f89d5a4ec7521b91909caf4fee89c997f4/server.jar",
    "20w49a": "https://piston-data.mojang.com/v1/objects/2fc0afe1fd31ca872761efbd2a7f635db234b359/server.jar",
    "20w51a": "https://piston-data.mojang.com/v1/objects/fc87ef4c3cf1c815809249cc00ccade233b22cf5/server.jar",
    "1.16.5-rc1": "https://piston-data.mojang.com/v1/objects/fc87ef4c3cf1c815809249cc00ccade233b22cf5/server.jar",
    "21w03a": "https://piston-data.mojang.com/v1/objects/dbe81ef81e20e76b1458be822026887fef84c541/server.jar",
    "21w05a": "https://piston-data.mojang.com/v1/objects/ff10b6f3bb37799e933ff0c2c300626b78ebfb1d/server.jar",
    "21w05b": "https://piston-data.mojang.com/v1/objects/f92547a92214ab71a58834e7453ab29a6ab2d192/server.jar",
    "21w06a": "https://piston-data.mojang.com/v1/objects/6290ba4b475fca4a74de990c7fd8eccffd9654dd/server.jar",
    "21w07a": "https://piston-data.mojang.com/v1/objects/99c3a9744719d0d401af63bb684cf1eb5231a75c/server.jar",
    "21w08a": "https://piston-data.mojang.com/v1/objects/d5e31633d884e190e046b8645f802541bec2a5e9/server.jar",
    "21w08b": "https://piston-data.mojang.com/v1/objects/801d5e25869bab291077c773913cc2b490427314/server.jar",
    "21w10a": "https://piston-data.mojang.com/v1/objects/5998d2c7c15fea04b2541efdcbec4c8cfe5df2a6/server.jar",
    "21w11a": "https://piston-data.mojang.com/v1/objects/c828957ad249138129ccbc8749bfd14f01d96a4b/server.jar",
    "21w13a": "https://piston-data.mojang.com/v1/objects/36d49b1a6d05f1deac293d477bfa2b4a1babb71c/server.jar",
    "21w14a": "https://piston-data.mojang.com/v1/objects/0cb279c49ea3afda25c9d7257bef650e8dc17429/server.jar",
    "21w15a": "https://piston-data.mojang.com/v1/objects/0a39422009a7aa01dd185043746c50dc909dc345/server.jar",
    "21w16a": "https://piston-data.mojang.com/v1/objects/b8bacc67a9db84db59e2f97e9a9fba3a242480a8/server.jar",
    "21w17a": "https://piston-data.mojang.com/v1/objects/ec995f939bb41a785f960985e73821c7044fc32e/server.jar",
    "21w18a": "https://piston-data.mojang.com/v1/objects/0b18d883bd1132f761aa715d6a97e29e54a9b8b6/server.jar",
    "21w19a": "https://piston-data.mojang.com/v1/objects/d0a9151432af384f5f2ca72e8e43422772158d0e/server.jar",
    "21w20a": "https://piston-data.mojang.com/v1/objects/054b2065dd63c3e4227879046beae7acaeb7e8d3/server.jar",
    "1.17-pre1": "https://piston-data.mojang.com/v1/objects/80a01a1178bcfb67b42636df3a9cdd275f3cc4d4/server.jar",
    "1.17-pre2": "https://piston-data.mojang.com/v1/objects/d8756c67ce3b3fe20d0510afb3e22fa16310b2e6/server.jar",
    "1.17-pre3": "https://piston-data.mojang.com/v1/objects/18abbb3f980fc9b05188535db45a67276ea41f90/server.jar",
    "1.17-pre4": "https://piston-data.mojang.com/v1/objects/528f491660bc5dc94c0d7911345a97438e5c1d86/server.jar",
    "1.17-pre5": "https://piston-data.mojang.com/v1/objects/31bb40019e8d6e64299abafd743f4d3e1a1a68b2/server.jar",
    "1.17-rc1": "https://piston-data.mojang.com/v1/objects/31bb40019e8d6e64299abafd743f4d3e1a1a68b2/server.jar",
    "1.17-rc2": "https://piston-data.mojang.com/v1/objects/1b6e0511e1e419fdcf5a81e53e36b5558032ee79/server.jar",
    "1.17.1-pre1": "https://piston-data.mojang.com/v1/objects/42dfafdd31a1e6edfe59c79ea0e109fede1c8071/server.jar",
    "1.17.1-pre2": "https://piston-data.mojang.com/v1/objects/e01e495461ecb834bb6a242bfea608af4f22b955/server.jar",
    "1.17.1-pre3": "https://piston-data.mojang.com/v1/objects/04750b5adff60610a5ba2cd3aa8102f7086c9301/server.jar",
    "1.17.1-rc1": "https://piston-data.mojang.com/v1/objects/b93cbcf6c65b92621d67b735e8610f7682f54694/server.jar",
    "1.17.1-rc2": "https://piston-data.mojang.com/v1/objects/dd9ca1bdc855535cd7ce0565f02285ad4d6d1ae5/server.jar",
    "21w37a": "https://piston-data.mojang.com/v1/objects/de695215d83f1f6ec5a19847f6178b84cfde7a26/server.jar",
    "21w38a": "https://piston-data.mojang.com/v1/objects/1283dff678ee5efb8e52d2fc77ec9d840317c6ca/server.jar",
    "21w39a": "https://piston-data.mojang.com/v1/objects/2b40ef4bf57b2040f7d9affb48c0131b228f954f/server.jar",
    "21w40a": "https://piston-data.mojang.com/v1/objects/84496ec4beeeae34a448b99f3e3d890066f6807f/server.jar",
    "21w41a": "https://piston-data.mojang.com/v1/objects/8eab49e576b21d6babfc60dcd14c68fac4926ab3/server.jar",
    "21w42a": "https://piston-data.mojang.com/v1/objects/cf518e2c80fdaef443d68d50d1ac23a72a0a7d85/server.jar",
    "21w43a": "https://piston-data.mojang.com/v1/objects/5c774a8b4e4407133eec7c4e1449c5f35974c589/server.jar",
    "21w44a": "https://piston-data.mojang.com/v1/objects/ae583fd57a8c07f2d6fbadce1ce1e1379bf4b32d/server.jar",
    "1.18-pre1": "https://piston-data.mojang.com/v1/objects/1c01e11c62ef7ce9b91324b570a1252d07544f18/server.jar",
    "1.18-pre2": "https://piston-data.mojang.com/v1/objects/c203586f5d2c02b417f0e104b65a8e5e7625b2f8/server.jar",
    "1.18-pre3": "https://piston-data.mojang.com/v1/objects/146d1809368fef552274122d9c380423c38068ab/server.jar",
    "1.18-pre4": "https://piston-data.mojang.com/v1/objects/d17d3501f7f9d68793d5a505978ea5b87a208b43/server.jar",
    "1.18-pre5": "https://piston-data.mojang.com/v1/objects/c29d03e9c6a21a3234a947e1025793c3cc40c13b/server.jar",
    "1.18-pre6": "https://piston-data.mojang.com/v1/objects/97b1c53df11cb8b973f4b522c8f4963b7e31495e/server.jar",
    "1.18-pre7": "https://piston-data.mojang.com/v1/objects/fe08544bb92ebe53070ec4a5f161ac19d8e9e4bb/server.jar",
    "1.18-pre8": "https://piston-data.mojang.com/v1/objects/051efe8853d00db6bef7f19324da25a465782376/server.jar",
    "1.18-rc1": "https://piston-data.mojang.com/v1/objects/81a2baf05f8f5bda41fac1542e7cc9d937bff41b/server.jar",
    "1.18-rc2": "https://piston-data.mojang.com/v1/objects/96162b8d0af608bee2febe602bdb46942e85f6d8/server.jar",
    "1.18-rc3": "https://piston-data.mojang.com/v1/objects/9a03d2c4ec2c737ce9d17a43d3774cdc0ea21030/server.jar",
    "1.18-rc4": "https://piston-data.mojang.com/v1/objects/5889357fe058d867f6e27ee3f033286c430ec91e/server.jar",
    "1.18.1-pre1": "https://piston-data.mojang.com/v1/objects/cd99e68b49c8a7db185d053518c6fb135cd04564/server.jar",
    "1.18.1-rc1": "https://piston-data.mojang.com/v1/objects/fa98951fb1fa1ca04d8d6283e91e667d91e6410d/server.jar",
    "1.18.1-rc2": "https://piston-data.mojang.com/v1/objects/653c704a89fe6437b363cff32ded037d5c0f6ec0/server.jar",
    "1.18.1-rc3": "https://piston-data.mojang.com/v1/objects/29c43f3af18e66f8368a16ec89f8e54ecda71d85/server.jar",
    "22w03a": "https://piston-data.mojang.com/v1/objects/686320be073916ae97b1ad78d22627809491dfc2/server.jar",
    "22w05a": "https://piston-data.mojang.com/v1/objects/e6183efda3cea1871cb090b37ec7e0305d6ebbde/server.jar",
    "22w06a": "https://piston-data.mojang.com/v1/objects/60c757a63f21877f8b053904ac76d04ff3cb76ef/server.jar",
    "22w07a": "https://piston-data.mojang.com/v1/objects/8131d9e36640d40ce8464c58035f35475579e897/server.jar",
    "1.18.2-pre1": "https://piston-data.mojang.com/v1/objects/c3e2734bafdb017efab854b01c66dd795722a332/server.jar",
    "1.18.2-pre2": "https://piston-data.mojang.com/v1/objects/888cb380db39a115cfe978c00922d24536bdd2a5/server.jar",
    "1.18.2-pre3": "https://piston-data.mojang.com/v1/objects/1c898afff0449eed08ad8036aaa4c652952035de/server.jar",
    "1.18.2-rc1": "https://piston-data.mojang.com/v1/objects/2f52c69c90d63c024548ae5c5438ff3156ece6c2/server.jar",
    "22w11a": "https://piston-data.mojang.com/v1/objects/a13b9678c60b0a84767e6cef0086c65cadac036e/server.jar",
    "22w12a": "https://piston-data.mojang.com/v1/objects/f238cf129a0848effe5037d8aaefe3f1f350b689/server.jar",
    "22w13a": "https://piston-data.mojang.com/v1/objects/7c8afca77bb9a73d31cdc70f2f68b4119d581455/server.jar",
    "22w14a": "https://piston-data.mojang.com/v1/objects/cf4f3a6492c0a84e2e852fe0ea714080923ab6ad/server.jar",
    "22w15a": "https://piston-data.mojang.com/v1/objects/2760f745a00711bcc19bf78d6056019f69318d03/server.jar",
    "22w16a": "https://piston-data.mojang.com/v1/objects/8ac6c67599bd30009fdc2f9d0174419b0bc19f8b/server.jar",
    "22w16b": "https://piston-data.mojang.com/v1/objects/a54810e8b1a7a043fa54a462309d680ad67da479/server.jar",
    "22w17a": "https://piston-data.mojang.com/v1/objects/9b4d5a87b48d7c3784fdfc9d6982543e8d9296df/server.jar",
    "22w18a": "https://piston-data.mojang.com/v1/objects/d3259a8939a724c78ebbb995dfc31c1c364464e3/server.jar",
    "22w19a": "https://piston-data.mojang.com/v1/objects/c354ac562b44fe5857535935125942ff89616cab/server.jar",
    "1.19-pre1": "https://piston-data.mojang.com/v1/objects/1be90ec671e145e56b789de428b63ec43a2d9721/server.jar",
    "1.19-pre2": "https://piston-data.mojang.com/v1/objects/6cc6cac49cd862ad9005816eb1ffc7dd4bd066dd/server.jar",
    "1.19-pre3": "https://piston-data.mojang.com/v1/objects/0702387c3519cc23a5184893275d00c05abf056d/server.jar",
    "1.19-pre4": "https://piston-data.mojang.com/v1/objects/a16331571233081eced58459a33254aa5a984a7d/server.jar",
    "1.19-pre5": "https://piston-data.mojang.com/v1/objects/1ba1b6389f00fa40a10af047fd7a76a9c68dba72/server.jar",
    "1.19-rc1": "https://piston-data.mojang.com/v1/objects/76ebdba03954e5a2185fb7a1d3a25096eb6bd195/server.jar",
    "1.19-rc2": "https://piston-data.mojang.com/v1/objects/d3250b1e5e0e8762ec8ceae034d5f229965d00d3/server.jar",
    "22w24a": "https://piston-data.mojang.com/v1/objects/fdad42550c3f0bcdc52680dcebd5b712d32bc5d7/server.jar",
    "1.19.1-pre1": "https://piston-data.mojang.com/v1/objects/a4d30a572176e81e115d36ec71bd2e67798ed14e/server.jar",
    "1.19.1-rc1": "https://piston-data.mojang.com/v1/objects/71a6d4c634de517ab1b6c2db8b743cbc831d9794/server.jar",
    "1.19.1-pre2": "https://piston-data.mojang.com/v1/objects/17354c4963fb0176ad34595927ce62e55ea3daf4/server.jar",
    "1.19.1-pre3": "https://piston-data.mojang.com/v1/objects/afbc14b0518843f189ed3ddd00f01b5881ef6513/server.jar",
    "1.19.1-pre4": "https://piston-data.mojang.com/v1/objects/0f7f0c876024d0a84cb50547f72fe81dbfbfdb19/server.jar",
    "1.19.1-pre5": "https://piston-data.mojang.com/v1/objects/33cdf9ceaaedebb0a71ca5f4d85d4e7198c09b8e/server.jar",
    "1.19.1-pre6": "https://piston-data.mojang.com/v1/objects/2cad39169c1a505ffca1049b236a4ddaf62c617d/server.jar",
    "1.19.1-rc2": "https://piston-data.mojang.com/v1/objects/5ec09b2700e5e83380a23cb18e66cfdaa931640b/server.jar",
    "1.19.1-rc3": "https://piston-data.mojang.com/v1/objects/e7ff323e06ccb32083b7cd2472dce3b9056e2940/server.jar",
    "1.19.2-rc1": "https://piston-data.mojang.com/v1/objects/ba8a776dc31a6093a07d3f4fbad1a8d680f8faf3/server.jar",
    "1.19.2-rc2": "https://piston-data.mojang.com/v1/objects/93649d39350077f998296138964e4591d4571140/server.jar",
    "22w42a": "https://piston-data.mojang.com/v1/objects/008996e2d1e0d49d7f1b477f69106a6d23c5c103/server.jar",
    "22w43a": "https://piston-data.mojang.com/v1/objects/6718a5ac0b073644dbdfbd25f8218c68a1b390db/server.jar",
    "22w44a": "https://piston-data.mojang.com/v1/objects/ed050b461b7dd347f383176ef03a71bacb844e69/server.jar",
    "22w45a": "https://piston-data.mojang.com/v1/objects/d98f05500b14a8884b85e71be9fa1ef0d261029a/server.jar",
    "22w46a": "https://piston-data.mojang.com/v1/objects/302ae4acba96e733fdbe144ebe2ba575b2bbf969/server.jar",
    "1.19.3-pre1": "https://piston-data.mojang.com/v1/objects/046fee78cd174105cb9b958a8459c0405ab19959/server.jar",
    "1.19.3-pre2": "https://piston-data.mojang.com/v1/objects/f8a18aa1e7b658de909470f69553c53d8662dfbe/server.jar",
    "1.19.3-pre3": "https://piston-data.mojang.com/v1/objects/323175facb90c05b07dff84b4cff39fd9cab138a/server.jar",
    "1.19.3-rc1": "https://piston-data.mojang.com/v1/objects/0c713920eff7358cb01c56979e8d732943bb893b/server.jar",
    "1.19.3-rc2": "https://piston-data.mojang.com/v1/objects/138c813e22102e1a82a1be7b76080f40235183fe/server.jar",
    "1.19.3-rc3": "https://piston-data.mojang.com/v1/objects/5f459ba58558d797229c819c0314bec84e774ecb/server.jar",
    "23w03a": "https://piston-data.mojang.com/v1/objects/b033d57035b293a9eda548db0615c1c89c21ea28/server.jar",
    "23w04a": "https://piston-data.mojang.com/v1/objects/2f31a8584ec1e70abd2d8b22d976feb52a6a3e31/server.jar",
    "23w05a": "https://piston-data.mojang.com/v1/objects/98cfa3f8f9aef61e1298c9cfd62f6eeaf8abe206/server.jar",
    "23w06a": "https://piston-data.mojang.com/v1/objects/daaed1fac98d17bd76f8fd43268f1c1b97230b59/server.jar",
    "23w07a": "https://piston-data.mojang.com/v1/objects/b919e6e1683a4b6f37f2717c7841e88e306bdc94/server.jar",
    "1.19.4-pre1": "https://piston-data.mojang.com/v1/objects/0bc471b96bb0edbc2f03e6cdc3ad981f7a4f5f8a/server.jar",
    "1.19.4-pre2": "https://piston-data.mojang.com/v1/objects/d0b48d637834e879c16de26ffc11226d2d8e6772/server.jar",
    "1.19.4-pre3": "https://piston-data.mojang.com/v1/objects/cedc29f7e4927bfe58c96e67495a73c7333c75cd/server.jar",
    "1.19.4-pre4": "https://piston-data.mojang.com/v1/objects/711aa1f63c20650789e9740d66ff55c3e8e4f2ae/server.jar",
    "1.19.4-rc1": "https://piston-data.mojang.com/v1/objects/c41c9653dc18634f52c010040177deabf9a878f2/server.jar",
    "1.19.4-rc2": "https://piston-data.mojang.com/v1/objects/8abd7d9568385ade54cdd8bf77306e637482711b/server.jar",
    "1.19.4-rc3": "https://piston-data.mojang.com/v1/objects/905778cc578c5a1757a9358a3feb5c19a0178fec/server.jar",
    "23w12a": "https://piston-data.mojang.com/v1/objects/92fdef90109e534d47e378124ab86e2d6d7b3a42/server.jar",
    "23w13a": "https://piston-data.mojang.com/v1/objects/701767d4d07aad992e3e2875ae5d1485cebf66e0/server.jar",
    "23w14a": "https://piston-data.mojang.com/v1/objects/cb67d34c44013759bca77085ae42e3a7b37f265d/server.jar",
    "23w16a": "https://piston-data.mojang.com/v1/objects/4a8487f877eb4f3506978fb85faf41a08b570398/server.jar",
    "23w17a": "https://piston-data.mojang.com/v1/objects/96e1b9db0f3d90309db34e8ce4fd39b52f6ddaa0/server.jar",
    "23w18a": "https://piston-data.mojang.com/v1/objects/240177c763b6009ea81aaf0ef14a73822320856d/server.jar",
    "1.20-pre1": "https://piston-data.mojang.com/v1/objects/95ac4bf3d2f4ae57687493f5232d3f58334b85d2/server.jar",
    "1.20-pre2": "https://piston-data.mojang.com/v1/objects/fce02f0ed50b4722f8ec58acef06275b91cde08d/server.jar",
    "1.20-pre3": "https://piston-data.mojang.com/v1/objects/6adffc7f05724f22b1644ecc191899e4beb33443/server.jar",
    "1.20-pre4": "https://piston-data.mojang.com/v1/objects/04b889e29aeffc23d2a3ebdd7e728184d9441e02/server.jar",
    "1.20-pre5": "https://piston-data.mojang.com/v1/objects/2b41aed1e7c7fecf11ca15bad03b0fa95eb4fbd9/server.jar",
    "1.20-pre6": "https://piston-data.mojang.com/v1/objects/c737b7411fc0b60426a9feca83d09d63f4a86f27/server.jar",
    "1.20-pre7": "https://piston-data.mojang.com/v1/objects/ed6ddd61aeb1f529ef626fae9bcb0a5f51491f71/server.jar",
    "1.20-rc1": "https://piston-data.mojang.com/v1/objects/0d9315f92842e35fcb6fddb10db3a13675a1ad04/server.jar",
    "1.20.1-rc1": "https://piston-data.mojang.com/v1/objects/6890ac51068a05e3fcc4158478247e5a5e47bcac/server.jar",
    "23w31a": "https://piston-data.mojang.com/v1/objects/11ef2ae139b0badda80a1ea07c2dd0cf9034a32f/server.jar",
    "23w32a": "https://piston-data.mojang.com/v1/objects/bfe1a408d8d809b206369fceab0e8a883226d0a6/server.jar",
    "23w33a": "https://piston-data.mojang.com/v1/objects/0254dde460b23861840cff6e80fc7fdbbccad88e/server.jar",
    "23w35a": "https://piston-data.mojang.com/v1/objects/6a2ac9eecb377f4894b84de711973edc751d0607/server.jar",
    "1.20.2-pre1": "https://piston-data.mojang.com/v1/objects/7fa1c9c59238ee98696da880d361d96c728dd9ea/server.jar",
    "1.20.2-pre2": "https://piston-data.mojang.com/v1/objects/cf5d9b2461898afd589274349989be704084a8dd/server.jar",
    "1.20.2-pre3": "https://piston-data.mojang.com/v1/objects/3d2eecdda5f6c7260d73aa5c2e5ce1a42e0f24e4/server.jar",
    "1.20.2-pre4": "https://piston-data.mojang.com/v1/objects/9f1b8f9918d5d8d59781886f33e5b7b2053d0486/server.jar",
    "1.20.2-rc1": "https://piston-data.mojang.com/v1/objects/70dad7e61afc2e255e73842760ef9461a00c852d/server.jar",
    "1.20.2-rc2": "https://piston-data.mojang.com/v1/objects/ef01ddc7ee3fd517f55f34259c411323673b6347/server.jar",
    "23w40a": "https://piston-data.mojang.com/v1/objects/0f51a81705f4694b92f5273ffa2c52c45f27b7f8/server.jar",
    "23w41a": "https://piston-data.mojang.com/v1/objects/e3e4c46324ac42b1789f7ff6e895ae3c843a9819/server.jar",
    "23w42a": "https://piston-data.mojang.com/v1/objects/b5f423ba1c4191d133c0284a2b1b36da46f8b5f8/server.jar",
    "23w43a": "https://piston-data.mojang.com/v1/objects/135f89e56c2d83d9ef0f7915f0cdf1047737d51a/server.jar",
    "23w43b": "https://piston-data.mojang.com/v1/objects/e7f9a4ca5ad3cadee399aa90f1d37f3ee94f292c/server.jar",
    "23w44a": "https://piston-data.mojang.com/v1/objects/009b4831cdda78d8f9b235265e45d0bf14a920da/server.jar",
    "23w45a": "https://piston-data.mojang.com/v1/objects/9c2b37701bf77ae22df4c32fd6dd1614049ce994/server.jar",
    "23w46a": "https://piston-data.mojang.com/v1/objects/2f30bbf9229e2dcbaf148eb9750df1d19ffa6d19/server.jar",
    "1.20.3-pre1": "https://piston-data.mojang.com/v1/objects/e5db7e4884f55c4dd986ca7200145759169e0045/server.jar",
    "1.20.3-pre2": "https://piston-data.mojang.com/v1/objects/5a76da0ae88eee28ab4c0fa2ffabb837a4572398/server.jar",
    "1.20.3-pre3": "https://piston-data.mojang.com/v1/objects/3802cf61288841f29f0af0d7c73ab58094be34cd/server.jar",
    "1.20.3-pre4": "https://piston-data.mojang.com/v1/objects/1567e8a24c547ac3a95ce41d24024a94e9c7299c/server.jar",
    "1.20.3-rc1": "https://piston-data.mojang.com/v1/objects/64cab4e87f8c2cad74d8bfc23df2cd193b4a615e/server.jar",
    "1.20.4-rc1": "https://piston-data.mojang.com/v1/objects/589a0babd82ff5a086e4085aa8a1dc46fecc222d/server.jar",
    "23w51a": "https://piston-data.mojang.com/v1/objects/e44e1d8c34f3020b0485ddd1436e91134b7de9a3/server.jar",
    "23w51b": "https://piston-data.mojang.com/v1/objects/d443ec98f3f3ee2dc92e0788d6d83d74844feb4f/server.jar",
    "24w03a": "https://piston-data.mojang.com/v1/objects/730a3ef2f99f6a822aa504bfee2eb5372d826293/server.jar",
    "24w03b": "https://piston-data.mojang.com/v1/objects/5b9a529dc40d8394cbd6203a8ebe66c8e2f86fd4/server.jar",
    "24w04a": "https://piston-data.mojang.com/v1/objects/d9f13751240a2fe4e85be1c839d9a4de1413c251/server.jar",
    "24w05a": "https://piston-data.mojang.com/v1/objects/cc0f01e6406fa8a2b50c3c06edef74e7a7bf74de/server.jar",
    "24w05b": "https://piston-data.mojang.com/v1/objects/189526bf25c06f7c0071aa637bc5f3668a6457d4/server.jar",
    "24w06a": "https://piston-data.mojang.com/v1/objects/703cffc390ff71b7900d7a4356f48bc2108b448e/server.jar",
    "24w07a": "https://piston-data.mojang.com/v1/objects/94acd52e9b9392e21a06231bdc4f8f0cd6ccb2af/server.jar",
    "24w09a": "https://piston-data.mojang.com/v1/objects/7c70922198a2d18e0252c315b55623b822b4e910/server.jar",
    "24w10a": "https://piston-data.mojang.com/v1/objects/9f8e96ebe4db0323653111b28df63f66395cb19d/server.jar",
    "24w11a": "https://piston-data.mojang.com/v1/objects/00cab0438130dc3e6ae91f53387bb96ae7986d31/server.jar",
    "24w12a": "https://piston-data.mojang.com/v1/objects/6f036460d361ce1e645bba365a72be2eed35ec01/server.jar",
    "24w13a": "https://piston-data.mojang.com/v1/objects/2fd2113b7b81cc78cb4a76939a6c11840d57036d/server.jar",
    "24w14a": "https://piston-data.mojang.com/v1/objects/960cb0e5c794b02abdbcdbdc15b4de058b222118/server.jar",
    "1.20.5-pre1": "https://piston-data.mojang.com/v1/objects/018c4aa3b1dcd5ac4487456de062072de750f729/server.jar",
    "1.20.5-pre2": "https://piston-data.mojang.com/v1/objects/c794b404663758cba43c67d097a25c5d4eb84a37/server.jar",
    "1.20.5-pre3": "https://piston-data.mojang.com/v1/objects/5ac067ccc569ef9e2177cf4331c8e82d3e072692/server.jar",
    "1.20.5-pre4": "https://piston-data.mojang.com/v1/objects/2793397cf42243a69fca37ff0887e8560a36c583/server.jar",
    "1.20.5-rc1": "https://piston-data.mojang.com/v1/objects/ec45f58d589dc1b00b25c6798dd10d2af70867e5/server.jar",
    "1.20.5-rc2": "https://piston-data.mojang.com/v1/objects/921814646156d838286dc0634a0031f042c6e0d2/server.jar",
    "1.20.5-rc3": "https://piston-data.mojang.com/v1/objects/7d735a8eda6797ed196141b76e96b46546bde091/server.jar",
    "1.20.6-rc1": "https://piston-data.mojang.com/v1/objects/a9b9c22721ec3ac516627f30554f21ed7c23efe5/server.jar",
    "24w18a": "https://piston-data.mojang.com/v1/objects/22618c686c86be630601e5d9fcf581674105c899/server.jar",
    "24w19a": "https://piston-data.mojang.com/v1/objects/8088cca48fece804d29b368ab5bbcc27a540456c/server.jar",
    "24w19b": "https://piston-data.mojang.com/v1/objects/447bfe84875399d44d383de7f534e1cc10bae9a5/server.jar",
    "24w20a": "https://piston-data.mojang.com/v1/objects/e3b1bcc2d7a09b6f1acfef7090ee64409feb3b94/server.jar",
    "24w21a": "https://piston-data.mojang.com/v1/objects/6ba7192e60bedb3ff02db3c57b75f7ea56c63242/server.jar",
    "24w21b": "https://piston-data.mojang.com/v1/objects/743d74805b64f83052fe449993f42182f76b129e/server.jar",
    "1.21-pre1": "https://piston-data.mojang.com/v1/objects/57e59ee5d8bc6ce664a7d76de45f8df9c110381f/server.jar",
    "1.21-pre2": "https://piston-data.mojang.com/v1/objects/3a8da3a1afcfb09d701fa17e405d09cd0c635748/server.jar",
    "1.21-pre3": "https://piston-data.mojang.com/v1/objects/96266e18a95faa1c785ac852315e886d0e8bb174/server.jar",
    "1.21-pre4": "https://piston-data.mojang.com/v1/objects/14b1a86d9fcfc82c013e82910e8209617c3a721e/server.jar",
    "1.21-rc1": "https://piston-data.mojang.com/v1/objects/902101d2fb0f968b9c0ddb8b8cff9afef23f72c7/server.jar",
    "1.21.1-rc1": "https://piston-data.mojang.com/v1/objects/e56720aba46f7f07238c4c054a160fc942da9f78/server.jar",
    "24w33a": "https://piston-data.mojang.com/v1/objects/90f9c80aeef3966343e661a1487b7918c90ae61d/server.jar",
    "24w34a": "https://piston-data.mojang.com/v1/objects/ff16e26392a5ced7cfe52ffdc5461cd646b9b65d/server.jar",
    "24w35a": "https://piston-data.mojang.com/v1/objects/93d259fdba93aa7d3c1763cfb0136295087e0de3/server.jar",
    "24w36a": "https://piston-data.mojang.com/v1/objects/30663a50aaf407751ae9e704758364ed9433206d/server.jar",
    "24w37a": "https://piston-data.mojang.com/v1/objects/4ba5f8917ac400474751b6e0f20d311d3b726fe7/server.jar"
}

## 12 APRIL'S FOOLS VERSIONS ADDED (2.0-blue - 24w14potato-reupload)
# LAST UPDATED: 10/08/2024
MC_APRILS = {
    # "Version name": "Download link"
    "2.0-blue": "https://archive.org/download/2point-0-blue/2point0_blue_server.jar",
    "2.0-red": "https://archive.org/download/2point-0-red/2point0_red_server.jar",
    "2.0-purple": "https://archive.org/download/2point-0-purple/2point0_purple_server.jar",
    "15w14a": "https://piston-data.mojang.com/v1/objects/f7d2bd26ce7893477fc1ca6e27b671345253bae4/server.jar",
    "1.RV-Pre1": "https://piston-data.mojang.com/v1/objects/f51d9489706f603be6be9716407f1dab5f7f2733/server.jar",
    "3D-Shareware-v1.34": "https://piston-data.mojang.com/v1/objects/ffd306fc2aaa884755c5a6bf9fbd87aed26dd78f/server.jar",
    "24w14infinite": "https://piston-data.mojang.com/v1/objects/c0711cd9608d1af3d6f05ac423dd8f4199780225/server.jar",
    "22w13oneBlockAtATime": "https://piston-data.mojang.com/v1/objects/5f48eea55c7fd1881d9c63835b15dfb5bbcd3a67/server.jar",
    "23w13a_or_b-original": "https://piston-data.mojang.com/v1/objects/7a9b53ec7999ce01b73a74f3ab9e7e520b09f0eb/server.jar",
    "23w13a_or_b-reupload": "https://piston-data.mojang.com/v1/objects/6241fc14ce7a659f371683a72aa24c155f60cce1/server.jar",
    "24w14potato-original": "https://piston-data.mojang.com/v1/objects/846d3fe65b6dab3f8bf929a601e1f83d801d919c/server.jar",
    "24w14potato-reupload": "https://piston-data.mojang.com/v1/objects/2d29eee4f5a71f323d20b36d623e2ec21dab74f7/server.jar"
}

## 9 COMBAT TEST VERSIONS ADDED (1.14.3 Combat Test - Combat Test 8c)
# LAST UPDATED: 06/09/2024
MC_COMBAT = {
    # "Version name": "Download link"
    "1.14.3 Combat Test": "https://piston-data.mojang.com/v1/objects/168ae89abc66fd4ee2d84c844cd980ddae26e784/server.jar",
    "Combat Test 2": "https://piston-data.mojang.com/v1/objects/dbed2de0763a834bfaa851c0478c56aeee654010/server.jar",
    "Combat Test 3": "https://piston-data.mojang.com/v1/objects/8f8ff833e6c775286a54935dad282f8499578f9a/server.jar",
    "Combat Test 4": "https://piston-data.mojang.com/v1/objects/4914bb3f9ae37dabdcbd68aa05eda1783f605336/server.jar",
    "Combat Test 5": "https://piston-data.mojang.com/v1/objects/0cc9a1582949297c8f1ca83b937c8d84ad295ffe/server.jar",
    "Combat Test 6": "https://piston-data.mojang.com/v1/objects/1c35c493ade7a39e2d02bcc326498aaab96f1a09/server.jar",
    "Combat Test 7c": "https://piston-data.mojang.com/v1/objects/53c43fdae7d2ed01bbb31a82d99e31b9348e2a4b/server.jar",
    "Combat Test 8b": "https://piston-data.mojang.com/v1/objects/635866257b4fc1ade528db8bd53ebbebb4816e5e/server.jar",
    "Combat Test 8c": "https://piston-data.mojang.com/v1/objects/b707c44ac1503ad179fde86c78d41aa4d0cc78a5/server.jar"
}

## 51 OLD VERSIONS ADDED (c1.4-reupload - b1.8.1)
# LAST UPDATED: 06/09/2024
MC_OLD = {
    # "Version name": "Download link"
    "c1.4-reupload": "https://files.betacraft.uk/server-archive/classic/c1.4-1422.jar",
    "c1.10": "https://files.betacraft.uk/server-archive/classic/c1.10.jar",
    "a0.1.0": "https://files.betacraft.uk/server-archive/alpha/a0.1.0.jar",
    "a0.1.1-reupload": "https://vault.omniarchive.uk/versions/java/server/alpha/a0.1.1-1707.jar",
    "a0.1.2_01": "https://files.betacraft.uk/server-archive/alpha/a0.1.2_01.jar",
    "a0.1.3": "https://files.betacraft.uk/server-archive/alpha/a0.1.3.jar",
    "a0.1.4": "https://files.betacraft.uk/server-archive/alpha/a0.1.4.jar",
    "a0.2.0": "https://files.betacraft.uk/server-archive/alpha/a0.2.0.jar",
    "a0.2.0_01": "https://files.betacraft.uk/server-archive/alpha/a0.2.0_01.jar",
    "a0.2.1": "https://files.betacraft.uk/server-archive/alpha/a0.2.1.jar",
    "a0.2.2": "https://files.betacraft.uk/server-archive/alpha/a0.2.2.jar",
    "a0.2.2_01": "https://files.betacraft.uk/server-archive/alpha/a0.2.2_01.jar",
    "a0.2.3": "https://files.betacraft.uk/server-archive/alpha/a0.2.3.jar",
    "a0.2.4": "https://files.betacraft.uk/server-archive/alpha/a0.2.4.jar",
    "a0.2.5-original": "https://files.betacraft.uk/server-archive/alpha/a0.2.5-0923.jar",
    "a0.2.5-reupload": "https://files.betacraft.uk/server-archive/alpha/a0.2.5-1004.jar",
    "a0.2.5_01": "https://files.betacraft.uk/server-archive/alpha/a0.2.5_01.jar",
    "a0.2.5_02": "https://files.betacraft.uk/server-archive/alpha/a0.2.5_02.jar",
    "a0.2.6": "https://files.betacraft.uk/server-archive/alpha/a0.2.6.jar",
    "a0.2.6_01": "https://files.betacraft.uk/server-archive/alpha/a0.2.6_01.jar",
    "a0.2.6_02": "https://files.betacraft.uk/server-archive/alpha/a0.2.6_02.jar",
    "a0.2.7": "https://files.betacraft.uk/server-archive/alpha/a0.2.7.jar",
    "a0.2.8": "https://files.betacraft.uk/server-archive/alpha/a0.2.8.jar",
    "b1.0": "https://files.betacraft.uk/server-archive/beta/b1.0.jar",
    "b1.0_01": "https://files.betacraft.uk/server-archive/beta/b1.0_01.jar",
    "b1.1": "https://files.betacraft.uk/server-archive/beta/b1.1.jar",
    "b1.1_01": "https://files.betacraft.uk/server-archive/beta/b1.1_01.jar",
    "b1.1_02": "https://files.betacraft.uk/server-archive/beta/b1.1_02.jar",
    "b1.2": "https://files.betacraft.uk/server-archive/beta/b1.2.jar",
    "b1.2_01": "https://files.betacraft.uk/server-archive/beta/b1.2_01.jar",
    "b1.3-original": "https://files.betacraft.uk/server-archive/beta/b1.3-1647.jar",
    "b1.3-reupload": "https://files.betacraft.uk/server-archive/beta/b1.3-1731.jar",
    "b1.4": "https://files.betacraft.uk/server-archive/beta/b1.4.jar",
    "b1.4_01": "https://files.betacraft.uk/server-archive/beta/b1.4_01.jar",
    "b1.5": "https://files.betacraft.uk/server-archive/beta/b1.5.jar",
    "b1.5_01": "https://files.betacraft.uk/server-archive/beta/b1.5_01.jar",
    "b1.5_02": "https://files.betacraft.uk/server-archive/beta/b1.5_02.jar",
    "b1.6_test_build_3": "https://files.betacraft.uk/server-archive/beta/prerelease/b1.6-tb3.jar",
    "b1.6_preview": "https://files.betacraft.uk/server-archive/beta/prerelease/b1.6-pre-trailer.jar",
    "b1.6": "https://files.betacraft.uk/server-archive/beta/b1.6.jar",
    "b1.6.1": "https://files.betacraft.uk/server-archive/beta/b1.6.1.jar",
    "b1.6.2": "https://files.betacraft.uk/server-archive/beta/b1.6.2.jar",
    "b1.6.3": "https://files.betacraft.uk/server-archive/beta/b1.6.3.jar",
    "b1.6.4": "https://files.betacraft.uk/server-archive/beta/b1.6.4.jar",
    "b1.6.5": "https://files.betacraft.uk/server-archive/beta/b1.6.5.jar",
    "b1.6.6": "https://files.betacraft.uk/server-archive/beta/b1.6.6.jar",
    "b1.7": "https://files.betacraft.uk/server-archive/beta/b1.7.jar",
    "b1.7_01": "https://files.betacraft.uk/server-archive/beta/b1.7_01.jar",
    "b1.7.2": "https://files.betacraft.uk/server-archive/beta/b1.7.2.jar",
    "b1.7.3": "https://files.betacraft.uk/server-archive/beta/b1.7.3.jar",
    "b1.8": "https://files.betacraft.uk/server-archive/beta/b1.8.jar",
    "b1.8.1": "https://files.betacraft.uk/server-archive/beta/b1.8.1.jar"
}
#################################
### THINGS TO DO/FIX - UPDATED: 12/09/2024 ###
# - [WIP] Add support for detailed logs.
# - [Pending] Test if old server versions work properly.
# - [Pending] Add more languages.
# - [Pending] Add a custom server.properties file for every version in order to avoid errors on old builds of Minecraft.
#################################
### DEVELOPER NOTES ###
# - Logging system needs to be improved.
#################################

#### PROGRAM ####

# SET-UP LOGGER
import logging
import os
from datetime import datetime
APPDATA = os.getenv('APPDATA')
SSTOOLS_FOLDER = os.path.join(APPDATA, "SSTools4MC") # type: ignore
LOG_PATH = os.path.join(SSTOOLS_FOLDER, "logs")
LOGGER = logging.getLogger('SSTools4MC') # logger name
LOGGER.setLevel(logging.DEBUG) # log level
current_date = datetime.now()
formatted_date = current_date.strftime('%Y-%m-%d')
log_file = os.path.join(LOG_PATH, f'{formatted_date}.log') # log file
if not os.path.exists(log_file):
    os.makedirs(LOG_PATH, exist_ok=True) # create log folder if it doesn't exist
    with open(log_file, 'w+'):
        pass # create log file if it doesn't exist
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S') # log format
file_handler.setFormatter(formatter)
LOGGER.addHandler(file_handler)
LOGGER.propagate = False # disable console logging
LOGGER.info('LOGGING STARTED...')

try:
    # SYSTEM LANGUAGE
    import locale
    SYSTEM_LANG = str(locale.getlocale()[0]) # get system language
    if SYSTEM_LANG.startswith('es') or SYSTEM_LANG.startswith('Spanish'):
        LOGGER.info('System language: Spanish')
    else:
        LOGGER.info('System language: English')

    # IMPORTS (INTERNAL)
    import sys
    import time
    import ctypes
    import webbrowser
    import subprocess
    from tkinter import filedialog
    from tkinter import messagebox

    # DEFAULTS
    # This variables are setted to None to handle errors
    valor = None
    runn = True

    # PATHS
    CONFIG_PATH = os.path.join(SSTOOLS_FOLDER, "config")
    SAVED_SERVERS = os.path.join(CONFIG_PATH, "saved-servers.cfg")

    # CHECK RELEASE TYPE
    if CHANNEL == 'dev':
        # Set dev channel parameters
        ICON_PATH = os.path.join(SSTOOLS_FOLDER, "assets", "icon-dev.ico")
        SSTITLE = "SSTools4MC (DEV)"
        LOGGER.info('Release type: DEV')
    elif CHANNEL == 'internal-testing':
        # Set internal testing parameters
        ICON_PATH = os.path.join(SSTOOLS_FOLDER, "assets", "icon-dev.ico")
        SSTITLE = "SSTools4MC (INTERNAL TESTING)"
        LOGGER.info('Release type: INTERNAL TESTING')
    else:
        # Set stable channel parameters
        ICON_PATH = os.path.join(SSTOOLS_FOLDER, "assets", "icon.ico")
        SSTITLE = "SSTools4MC"
        LOGGER.info('Release type: STABLE')

    # CHANGE WINDOW TITLE
    def window_title(title):
        os.system(f'title {title}')
        LOGGER.info(f'Window title changed to: {title}')

    # PROGRAM STARTING TITLE
    LOGGER.info(f'{SSTITLE} is starting...')
    if SYSTEM_LANG.startswith('es') or SYSTEM_LANG.startswith('Spanish'):
        window_title(f'{SSTITLE} está iniciando...')
        print(f'{SSTITLE} está iniciando...')
    else:
        window_title(f'{SSTITLE} is starting...')
        print(f'{SSTITLE} is starting...')

    # IMPORTS (EXTERNAL)
    for lib, func in NEEDED_MODULES.items(): # try to import needed modules from the dictionary
        try:
            if func == '': # if the function is empty, import the whole module
                exec(f'import {lib}')
                LOGGER.info(f'Module "{lib}" imported successfully')
            else: # if the function is not empty, import it from the corresponding module
                exec(f'from {lib} import {func}')
                LOGGER.info(f'Function "{func}" from module "{lib}" imported successfully')
        except ImportError: # if the module is not found, try to install it
            LOGGER.warning(f'Module "{lib}" not found. Trying to install it...')
            if SYSTEM_LANG.startswith('es') or SYSTEM_LANG.startswith('Spanish'):
                print(f"- Instalando módulo necesario: {lib}")
            else:
                print(f"- Installing needed module: {lib}")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", lib], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                if func == '': # if the function is empty, import the whole module
                    LOGGER.info(f'Module "{lib}" installed successfully. Importing...')
                    exec(f'import {lib}')
                else: # if the function is not empty, import it from the corresponding module
                    LOGGER.info(f'Module "{lib}" installed successfully. Importing "{func}" function...')
                    exec(f'from {lib} import {func}')
            except Exception: # if the module or function can't be installed or accessed, show an error message and exit the program
                LOGGER.critical(f'Error with module "{lib}". Please retry or install it manually.')
                if SYSTEM_LANG.startswith('es') or SYSTEM_LANG.startswith('Spanish'):
                    messagebox.showerror("Error", f"No se pudo acceder al módulo '{lib}'. Por favor, reintenta abrir el programa o instálalo manualmente.")
                else:
                    messagebox.showerror("Error", f"Couldn't access '{lib}' module. Please try reopening the program or install it manually.")
                sys.exit(1)

    # CLS
    def cls():
        os.system('cls') # clear console
        LOGGER.info('Console cleared')

    # BRING WINDOW TO FRONT
    def front():
        os.system('echo ShowConsole') # this command brings the console window to front
        LOGGER.info('Window brought to front')

    # GET DATE
    def getdate():
        dayy = str(datetime.now().strftime("%d/%m/%Y")) # get current date to use in titles (day/month/year)
        return dayy

    # ENGLISH
    def eng():
        # SERVER STARTUP
        def ram():
            LOGGER.info('Entering Server Startup menu...')
            global servername
            cls()
            sservers = {}
            if os.path.exists(SAVED_SERVERS):
                with open(SAVED_SERVERS, 'r') as file: # read saved servers file
                    for line in file:
                        line = line.strip()
                        if line and not line.startswith('#'):
                            key, value = line.split('<[=]>')
                            sservers[key.strip()] = value.strip()
                if sservers: # if there are saved servers, show the list
                    cls()
                    window_title(f'{SSTITLE} - "Your Servers" list')
                    day = getdate()
                    print(f'{SSTITLE} - {day}\n--------------------------\n\n"Your Servers" List\n')
                    server_keys = list(sservers.keys())
                    for i, key in enumerate(server_keys, start=1): # print saved servers from loaded list
                        print(f"({i}) {key}")
                    nserv = colored("Add","cyan") # type: ignore
                    delserv = colored("Delete","red") # type: ignore
                    clearlist = colored("Clear","magenta") # type: ignore
                    print(f"\n(N) {nserv} Server\n(D) {delserv} a Server from the list\n(C) {clearlist} List\n(R) Return to main menu")
                    servsel = input("\nSelect one of the options or enter the number of the server to start= ").replace(" ", "")
                    try:
                        if servsel.lower() == "n":
                            newserv = filedialog.askdirectory()
                            front()
                            servname = os.path.basename(newserv)
                            server_jar_path = os.path.join(newserv, "server.jar")
                            if newserv == "" or servname == "":
                                newserv = False
                                servname = False
                            if newserv and servname and os.path.isfile(server_jar_path):
                                servname = colored(servname, "yellow") # type: ignore
                                with open(SAVED_SERVERS, 'r') as file:
                                    lines = file.readlines()
                                    servstring = f"{servname}<[=]>{newserv}\n"
                                    if servstring not in lines:
                                        os.makedirs(CONFIG_PATH, exist_ok=True)
                                        with open(SAVED_SERVERS, 'r+') as file:
                                            file.write(servstring)
                            else:
                                cls()
                                window_title(f'{SSTITLE} - You must select a valid server folder')
                                day = getdate()
                                print(f'{SSTITLE} - {day}\n--------------------------\n\nYou must select a valid server folder to save it in "Your Servers" List.')
                                time.sleep(2.5)
                                ram()
                            cls()
                            window_title(f'{SSTITLE} - Server saved')
                            day = getdate()
                            print(f'{SSTITLE} - {day}\n--------------------------\n\nThe server "{servname}" has been saved.')
                            time.sleep(1.5)
                            ram()
                        elif servsel.lower() == "d":
                            def servdel():
                                cls()
                                window_title(f'{SSTITLE} - Delete a server')
                                day = getdate()
                                print(f"{SSTITLE} - {day}\n--------------------------\n\nSelect the server to delete from the list.\n")
                                for i, key in enumerate(server_keys, start=1):
                                    print(f"({i}) {key}")
                                print("\n(N) Cancel\n(R) Return to main menu")
                                servsel = input("\nSelect one of the options or enter the number of the server to delete= ").replace(" ", "")
                                try:
                                    if servsel.lower() == "r":
                                        eng()
                                    elif servsel.lower() == "n":
                                        ram()
                                    else:
                                        if any(char in "0123456789+-*/" for char in servsel):
                                            if not servsel[0].isalpha():
                                                servv = eval(servsel)
                                            else:
                                                servv = servsel
                                        else:
                                            servv = servsel
                                        servsel = int(servv)
                                        if 1 <= servsel <= len(server_keys):
                                            servsel = server_keys[servsel - 1]
                                            servpath = sservers[servsel]
                                            servestring = f"{servsel}<[=]>{servpath}\n"
                                        os.makedirs(CONFIG_PATH, exist_ok=True)
                                        with open(SAVED_SERVERS, 'r') as file:
                                            lines = file.readlines()
                                            os.makedirs(CONFIG_PATH, exist_ok=True)
                                            with open(SAVED_SERVERS, 'w') as file:
                                                for line in lines:
                                                    if line != servestring:
                                                        file.write(line)
                                        cls()
                                        window_title(f'{SSTITLE} - Server deleted')
                                        day = getdate()
                                        print(f'{SSTITLE} - {day}\n--------------------------\n\nThe server "{servsel}" has been deleted from the list.')
                                        time.sleep(1.5)
                                        ram()             
                                except (ValueError, SyntaxError, IndexError, ZeroDivisionError):
                                    servdel()
                            servdel()
                        elif servsel.lower() == "c":
                            def lisclear():
                                cls()
                                yess = colored("Yes","green") # type: ignore
                                noo = colored("No","red") # type: ignore
                                window_title(f'{SSTITLE} - Are you sure?')
                                day = getdate()
                                clearconfirm = input(f'{SSTITLE} - {day}\n--------------------------\n\nAre you sure you want to clear the "Your Servers" List?\n\n(1) {yess}\n(2) {noo}\n\nSelect one of the options= ')
                                try:
                                    if any(char in "0123456789+-*/" for char in clearconfirm):
                                        if not clearconfirm[0].isalpha():
                                            clearconf = eval(clearconfirm)
                                        else:
                                            clearconf = clearconfirm
                                    else:
                                        clearconf = clearconfirm
                                    clearconf = int(clearconf)
                                    if clearconf == 1:
                                        os.makedirs(CONFIG_PATH, exist_ok=True)
                                        with open(SAVED_SERVERS, 'w') as file:
                                            file.write("# SSTools4MC\n# Saved servers\n")
                                        cls()
                                        window_title(f'{SSTITLE} - List cleared')
                                        day = getdate()
                                        print(f'{SSTITLE} - {day}\n--------------------------\n\nThe "Your Servers" List has been cleared.')
                                        time.sleep(1.5)
                                        ram()
                                    elif clearconf == 2:
                                        ram()
                                except (ValueError, SyntaxError, IndexError, ZeroDivisionError):
                                    lisclear()
                            lisclear()
                        elif servsel.lower() == "r":
                            eng()
                        else:
                            if any(char in "0123456789+-*/" for char in servsel):
                                if not servsel[0].isalpha():
                                    servv = eval(servsel)
                                else:
                                    servv = servsel
                            else:
                                servv = servsel
                            servsel = int(servv)
                            if 1 <= servsel <= len(server_keys):
                                servsel = server_keys[servsel - 1]
                                servpath = sservers[servsel]
                                os.makedirs(servpath, exist_ok=True)
                                os.chdir(servpath)
                                servername = servsel
                    except (ValueError, SyntaxError, IndexError, ZeroDivisionError):
                        ram()
                else:
                    os.makedirs(CONFIG_PATH, exist_ok=True)
                    with open(SAVED_SERVERS, 'w') as file:
                        file.write("# SSTools4MC\n# Saved servers\n")
                    cls()
                    adds = colored("Add a Server","cyan") # type: ignore
                    window_title(f'{SSTITLE} - There are no saved servers.')
                    day = getdate()
                    saveconfirm = input(f"{SSTITLE} - {day}\n--------------------------\n\nThere are no saved servers.\n\n(1) {adds}\n(2) Return to main menu\n\nSelect one of the options= ")
                    try:
                        if any(char in "0123456789+-*/" for char in saveconfirm):
                            if not saveconfirm[0].isalpha():
                                saveconf = eval(saveconfirm)
                            else:
                                saveconf = saveconfirm
                        else:
                            saveconf = saveconfirm
                        saveconf = int(saveconf)
                        if saveconf == 1:
                            newserv = filedialog.askdirectory()
                            front()
                            servname = os.path.basename(newserv)
                            server_jar_path = os.path.join(newserv, "server.jar")
                            if newserv == "" or servname == "":
                                newserv = False
                                servname = False
                            if newserv and servname and os.path.isfile(server_jar_path):
                                servname = colored(servname, "yellow") # type: ignore
                                with open(SAVED_SERVERS, 'r') as file:
                                    lines = file.readlines()
                                    servstring = f"{servname}<[=]>{newserv}\n"
                                    if servstring not in lines:
                                        os.makedirs(CONFIG_PATH, exist_ok=True)
                                        with open(SAVED_SERVERS, 'r+') as file:
                                            file.write(servstring)
                            else:
                                cls()
                                window_title(f'{SSTITLE} - You must select a valid server folder')
                                day = getdate()
                                print(f'{SSTITLE} - {day}\n--------------------------\n\nYou must select a valid server folder to save it in "Your Servers" List.')
                                time.sleep(2.5)
                                ram()
                            cls()
                            window_title(f'{SSTITLE} - Server saved')
                            day = getdate()
                            print(f'{SSTITLE} - {day}\n--------------------------\n\nThe server "{servname}" has been saved.')
                            time.sleep(1.5)
                            ram()
                            cls()
                            window_title(f'{SSTITLE} - Server saved')
                            day = getdate()
                            print(f'{SSTITLE} - {day}\n--------------------------\n\nThe server "{servname}" has been saved.')
                            time.sleep(1.5)
                            ram()
                        elif saveconf == 2:
                            eng()
                        else:
                            ram()
                    except (ValueError, SyntaxError, IndexError, ZeroDivisionError):
                        ram()
            else:
                os.makedirs(CONFIG_PATH, exist_ok=True)
                with open(SAVED_SERVERS, 'w') as file:
                    file.write("# SSTools4MC\n# Saved servers\n")
                cls()
                window_title(f'{SSTITLE} - There are no saved servers')
                day = getdate()
                input(f'{SSTITLE} - {day}\n--------------------------\n\nThere are no saved servers.\n\nPress ENTER to select a folder with a Server and add it to "Your Servers" list.')
                newserv = filedialog.askdirectory()
                front()
                servname = os.path.basename(newserv)
                server_jar_path = os.path.join(newserv, "server.jar")
                if newserv == "" or servname == "":
                    newserv = False
                    servname = False
                if newserv and servname and os.path.isfile(server_jar_path):
                    servname = colored(servname, "yellow") # type: ignore
                    with open(SAVED_SERVERS, 'r') as file:
                        lines = file.readlines()
                        servstring = f"{servname}<[=]>{newserv}\n"
                        if servstring not in lines:
                            os.makedirs(CONFIG_PATH, exist_ok=True)
                            with open(SAVED_SERVERS, 'r+') as file:
                                file.write(servstring)
                else:
                    cls()
                    window_title(f'{SSTITLE} - You must select a valid server folder')
                    day = getdate()
                    print(f'{SSTITLE} - {day}\n--------------------------\n\nYou must select a valid server folder to save it in "Your Servers" List.')
                    time.sleep(2.5)
                    ram()
                cls()
                window_title(f'{SSTITLE} - Server saved')
                day = getdate()
                print(f'{SSTITLE} - {day}\n--------------------------\n\nThe server "{servname}" has been saved.')
                time.sleep(1.5)
                ram()
                cls()
                window_title(f'{SSTITLE} - Server saved')
                day = getdate()
                print(f'{SSTITLE} - {day}\n--------------------------\n\nThe server "{servname}" has been saved.')
                time.sleep(1.5)
                ram()
            if os.path.exists("server.jar"):
                # CONFIG
                def config():
                    global nameserver
                    cls()
                    props = "server.properties"
                    if os.path.exists(props):
                        global properties
                        properties = {}
                        online = "Error"
                        hard = "Error"
                        pvp = "Error"
                        with open('server.properties', 'r') as file:
                            for line in file:
                                line = line.strip()
                                if line and not line.startswith('#'):
                                    key, value = line.split('=')
                                    properties[key.strip()] = value.strip()
                        if properties["online-mode"] == "false":
                            online = colored("ENABLE","green") # type: ignore
                        elif properties["online-mode"] == "true":
                            online = colored("DISABLE","red") # type: ignore
                        if properties["hardcore"] == "false":
                            hard = colored("ENABLE","green") # type: ignore
                        elif properties["hardcore"] == "true":
                            hard = colored("DISABLE","red") # type: ignore
                        if properties["pvp"] == "false":
                            pvp = colored("ENABLE","green") # type: ignore
                        elif properties["pvp"] == "true":
                            pvp = colored("DISABLE","red") # type: ignore
                        cls()
                        window_title(f'{SSTITLE} - Server management')
                        day = getdate()
                        confsel = input(f'{SSTITLE} - {day}\n--------------------------\n\nLets manage "{nameserver}"!\n\n(1) {online} online mode\n(2) {hard} hardcore mode\n(3) {pvp} PvP\n(4) Change gamemode\n(5) Change difficulty\n(6) Change max players limit\n(7) Back\n(8) Return to main menu\n\nSelect one of the options= ')
                        if properties["online-mode"] == "false":
                            online = "ENABLE"
                        elif properties["online-mode"] == "true":
                            online = "DISABLE"
                        if properties["hardcore"] == "false":
                            hard = "ENABLE"
                        elif properties["hardcore"] == "true":
                            hard = "DISABLE"
                        if properties["pvp"] == "false":
                            pvp = "ENABLE"
                        elif properties["pvp"] == "true":
                            pvp = "DISABLE"
                        try:
                            if any(char in "0123456789+-*/" for char in confsel):
                                if not confsel[0].isalpha():
                                    confug = eval(confsel)
                                else:
                                    confug = confsel
                            else:
                                confug = confsel
                            confug = int(confug) 
                            if confug == 1:
                                if online == "ENABLE":
                                    properties["online-mode"] = "true"
                                    with open('server.properties', 'w') as file:
                                        for key, value in properties.items():
                                            file.write(f'{key}={value}\n')
                                    online = colored("ENABLED","green") # type: ignore
                                elif online == "DISABLE":
                                    properties["online-mode"] = "false"
                                    with open('server.properties', 'w') as file:
                                        for key, value in properties.items():
                                            file.write(f'{key}={value}\n')
                                    online = colored("DISABLED","red") # type: ignore
                                cls()
                                window_title(f'{SSTITLE} - Online mode toggled')
                                day = getdate()
                                print(f"{SSTITLE} - {day}\n--------------------------\n\nOnline mode has been {online}.")
                                time.sleep(1.5)
                                config()
                            elif confug == 2:
                                if hard == "ENABLE":
                                    properties["hardcore"] = "true"
                                    with open('server.properties', 'w') as file:
                                        for key, value in properties.items():
                                            file.write(f'{key}={value}\n')
                                    hard = colored("ENABLED","green") # type: ignore
                                elif hard == "DISABLE":
                                    properties["hardcore"] = "false"
                                    with open('server.properties', 'w') as file:
                                        for key, value in properties.items():
                                            file.write(f'{key}={value}\n')
                                    hard = colored("DISABLED","red") # type: ignore
                                cls()
                                window_title(f'{SSTITLE} - Hardcore mode toggled')
                                day = getdate()
                                print(f"{SSTITLE} - {day}\n--------------------------\n\nHardcore mode has been {hard}.")
                                time.sleep(1.5)
                                config()
                            elif confug == 3:
                                if pvp == "ENABLE":
                                    properties["pvp"] = "true"
                                    with open('server.properties', 'w') as file:
                                        for key, value in properties.items():
                                            file.write(f'{key}={value}\n')
                                    pvp = colored("ENABLED","green") # type: ignore
                                elif pvp == "DISABLE":
                                    properties["pvp"] = "false"
                                    with open('server.properties', 'w') as file:
                                        for key, value in properties.items():
                                            file.write(f'{key}={value}\n')
                                    pvp = colored("DISABLED","red") # type: ignore
                                cls()
                                window_title(f'{SSTITLE} - PvP toggled')
                                day = getdate()
                                print(f"{SSTITLE} - {day}\n--------------------------\n\nPvP has been {pvp}.")
                                time.sleep(1.5)
                                config()
                            elif confug == 4:
                                def juego():
                                    global properties
                                    modo = properties["gamemode"]
                                    if modo == "survival" or modo == "0":
                                        modo = colored("SURVIVAL","cyan") # type: ignore
                                    elif modo == "creative" or modo == "1":
                                        modo = colored("CREATIVE","cyan") # type: ignore
                                    elif modo == "adventure" or modo == "2":
                                        modo = colored("ADVENTURE","cyan") # type: ignore
                                    elif modo == "spectator" or modo == "3":
                                        modo = colored("SPECTATOR","cyan") # type: ignore
                                    superv = colored("SURVIVAL","yellow") # type: ignore
                                    creat = colored("CREATIVE","yellow") # type: ignore
                                    avent = colored("ADVENTURE","yellow") # type: ignore
                                    espect = colored("SPECTATOR","yellow") # type: ignore
                                    cls()
                                    window_title(f'{SSTITLE} - Gamemode configuration')
                                    day = getdate()
                                    modosel = input(f"{SSTITLE} - {day}\n--------------------------\n\nThe current game mode is {modo}.\n\n(1) Change to {superv} gamemode\n(2) Change to {creat} gamemode\n(3) Change to {avent} gamemode\n(4) Change to {espect} gamemode\n(5) Go back\n(6) Return to main menu\n\nSelect one of the options= ")
                                    try:
                                        if any(char in "0123456789+-*/" for char in modosel):
                                            if not modosel[0].isalpha():
                                                coonf = eval(modosel)
                                            else:
                                                coonf = modosel
                                        else:
                                            coonf = modosel
                                        coonf = int(coonf)
                                        if coonf == 1:
                                            properties["gamemode"] = "0"
                                            with open('server.properties', 'w') as file:
                                                for key, value in properties.items():
                                                    file.write(f'{key}={value}\n')
                                            cls()
                                            window_title(f'{SSTITLE} - Gamemode is now set to Survival')
                                            day = getdate()
                                            print(f"{SSTITLE} - {day}\n--------------------------\n\nGamemode is now set to {superv}.")
                                            time.sleep(1.5)
                                            juego()
                                        elif coonf == 2:
                                            properties["gamemode"] = "1"
                                            with open('server.properties', 'w') as file:
                                                for key, value in properties.items():
                                                    file.write(f'{key}={value}\n')
                                            cls()
                                            window_title(f'{SSTITLE} - Gamemode is now set to Creative')
                                            day = getdate()
                                            print(f"{SSTITLE} - {day}\n--------------------------\n\nGamemode is now set to {creat}.")
                                            time.sleep(1.5)
                                            juego()
                                        elif coonf == 3:
                                            properties["gamemode"] = "2"
                                            with open('server.properties', 'w') as file:
                                                for key, value in properties.items():
                                                    file.write(f'{key}={value}\n')
                                            cls()
                                            window_title(f'{SSTITLE} - Gamemode is now set to Adventure')
                                            day = getdate()
                                            print(f"{SSTITLE} - {day}\n--------------------------\n\nGamemode is now set to {avent}.")
                                            time.sleep(1.5)
                                            juego()
                                        elif coonf == 4:
                                            properties["gamemode"] = "3"
                                            with open('server.properties', 'w') as file:
                                                for key, value in properties.items():
                                                    file.write(f'{key}={value}\n')
                                            cls()
                                            window_title(f'{SSTITLE} - Gamemode is now set to Spectator')
                                            day = getdate()
                                            print(f"{SSTITLE} - {day}\n--------------------------\n\nGamemode is now set to {espect}.")
                                            time.sleep(1.5)
                                            juego()
                                        elif coonf == 5:
                                            config()
                                        elif coonf == 6:
                                            eng()
                                        else:
                                            juego()
                                    except (ValueError, SyntaxError, IndexError, ZeroDivisionError):
                                        juego()
                                juego()
                            elif confug == 5:
                                def difconf():
                                    global properties
                                    dificultad = properties["difficulty"]
                                    if dificultad == "peaceful" or dificultad == "0":
                                        dificultad = colored("PEACEFUL","cyan") # type: ignore
                                    elif dificultad == "easy" or dificultad == "1":
                                        dificultad = colored("EASY","cyan") # type: ignore
                                    elif dificultad == "normal" or dificultad == "2":
                                        dificultad = colored("NORMAL","cyan") # type: ignore
                                    elif dificultad == "hard" or dificultad == "3":
                                        dificultad = colored("HARD","cyan") # type: ignore
                                    pacif = colored("PEACEFUL","yellow") # type: ignore
                                    facil = colored("EASY","yellow") # type: ignore
                                    normal = colored("NORMAL","yellow") # type: ignore
                                    dificil = colored("HARD","yellow") # type: ignore
                                    cls()
                                    window_title(f'{SSTITLE} - Difficulty configuration')
                                    day = getdate()
                                    difsel = input(f"{SSTITLE} - {day}\n--------------------------\n\nThe current difficulty is {dificultad}.\n\n(1) Change difficulty to {pacif}\n(2) Change difficulty to {facil}\n(3) Change difficulty to {normal}\n(4) Change difficulty to {dificil}\n(5) Go back\n(6) Return to main menu\n\nSelect one of the options= ")
                                    try:
                                        if any(char in "0123456789+-*/" for char in difsel):
                                            if not difsel[0].isalpha():
                                                difcc = eval(difsel)
                                            else:
                                                difcc = difsel
                                        else:
                                            difcc = difsel
                                        difcc = int(difcc)
                                        if difcc == 1:
                                            properties["difficulty"] = "0"
                                            with open('server.properties', 'w') as file:
                                                for key, value in properties.items():
                                                    file.write(f'{key}={value}\n')
                                            cls()
                                            window_title(f'{SSTITLE} - Difficulty is now set to Peaceful')
                                            day = getdate()
                                            print(f"{SSTITLE} - {day}\n--------------------------\n\nDifficulty is now set to {pacif}.")
                                            time.sleep(1.5)
                                            difconf()
                                        elif difcc == 2:
                                            properties["difficulty"] = "1"
                                            with open('server.properties', 'w') as file:
                                                for key, value in properties.items():
                                                    file.write(f'{key}={value}\n')
                                            cls()
                                            window_title(f'{SSTITLE} - Difficulty is now set to Easy')
                                            day = getdate()
                                            print(f"{SSTITLE} - {day}\n--------------------------\n\nDifficulty is now set to {facil}.")
                                            time.sleep(1.5)
                                            difconf()
                                        elif difcc == 3:
                                            properties["difficulty"] = "2"
                                            with open('server.properties', 'w') as file:
                                                for key, value in properties.items():
                                                    file.write(f'{key}={value}\n')
                                            cls()
                                            window_title(f'{SSTITLE} - Difficulty is now set to Normal')
                                            day = getdate()
                                            print(f"{SSTITLE} - {day}\n--------------------------\n\nDifficulty is now set to {normal}.")
                                            time.sleep(1.5)
                                            difconf()
                                        elif difcc == 4:
                                            properties["difficulty"] = "3"
                                            with open('server.properties', 'w') as file:
                                                for key, value in properties.items():
                                                    file.write(f'{key}={value}\n')
                                            cls()
                                            window_title(f'{SSTITLE} - Difficulty is now set to Hard')
                                            day = getdate()
                                            print(f"{SSTITLE} - {day}\n--------------------------\n\nDifficulty is now set to {dificil}.")
                                            time.sleep(1.5)
                                            difconf()
                                        elif difcc == 5:
                                            config()
                                        elif difcc == 6:
                                            eng()
                                        else:
                                            difconf()
                                    except (ValueError, SyntaxError, IndexError, ZeroDivisionError):
                                        difconf()
                                difconf()
                            elif confug == 6:
                                def playct():
                                    global properties
                                    players = colored(properties["max-players"],"cyan") # type: ignore
                                    cls()
                                    window_title(f'{SSTITLE} - Player limit configuration')
                                    day = getdate()
                                    newpl = input(f"{SSTITLE} - {day}\n--------------------------\n\nThe current player limit is a maximum of {players}.\n\n(N) Go back\n(M) Return to main menu\n\nSelect one of the options or enter the new player limit= ").replace(" ", "")
                                    try:
                                        if newpl.lower() == "n":
                                            config()
                                        elif newpl.lower() == "m":
                                            eng()
                                        else:
                                            if any(char in "0123456789+-*/" for char in newpl):
                                                if not newpl[0].isalpha():
                                                    entero = eval(newpl)
                                                else:
                                                    entero = newpl
                                            else:
                                                entero = newpl
                                            entero = int(entero)
                                            if entero <= 0 or entero > 100000:
                                                cls()
                                                window_title(f'{SSTITLE} - Invalid player limit')
                                                day = getdate()
                                                print(f"{SSTITLE} - {day}\n--------------------------\n\nEnter a valid number between 1 and 100,000.")
                                                time.sleep(1.5)
                                                playct()
                                            else:
                                                properties["max-players"] = entero
                                                with open('server.properties', 'w') as file:
                                                    for key, value in properties.items():
                                                        file.write(f'{key}={value}\n')
                                                entero = colored(str(entero),"yellow") # type: ignore
                                                cls()
                                                window_title(f'{SSTITLE} - Player limit changed')
                                                day = getdate()
                                                print(f"{SSTITLE} - {day}\n--------------------------\n\nThe maximum player limit is now {entero}.")
                                                time.sleep(1.5)
                                                playct()
                                    except (ValueError, SyntaxError, IndexError, ZeroDivisionError):
                                        playct()
                                playct()
                            elif confug == 7:
                                run_server()
                            elif confug == 8:
                                eng()
                            else:
                                config()
                        except (ValueError, SyntaxError, IndexError, ZeroDivisionError):
                            config()
                    else:
                        cls()
                        window_title(f'{SSTITLE} - Server configuration files not found :(')
                        day = getdate()
                        input(f"{SSTITLE} - {day}\n--------------------------\n\nThe server configuration files do not exist yet or are not available.\nYou must start the server properly at least once before you can configure it.\n\nPress ENTER to continue.")
                        run_server()
                def run_server():
                    global servername
                    global valor
                    global nameserver
                    valor1 = None
                    gbormb = None
                    vjava = None
                    if valor == None:
                        valor = "GB"
                        valor1 = colored("GIGABYTES","cyan") # type: ignore
                        vjava = "G"
                        gbormb = colored("MEGABYTES","yellow") # type: ignore
                    if valor == "GB":
                        valor1 = colored("GIGABYTES","cyan") # type: ignore
                        vjava = "G"
                        gbormb = colored("MEGABYTES","yellow") # type: ignore
                    elif valor == "MB":
                        valor1 = colored("MEGABYTES","cyan") # type: ignore
                        vjava = "M"
                        gbormb = colored("GIGABYTES","yellow") # type: ignore
                    nameserver = servername
                    cls()
                    gbs = 0
                    window_title(f'{SSTITLE} - You are about to start the server!')
                    day = getdate()
                    rammount = input(f'{SSTITLE} - {day}\n--------------------------\n\nYou are about to start the Server "{nameserver}"\n\n(M) Manage Server\n(C) Use RAM in {gbormb}\n(B) Back\n(N) Return to main menu\n\nSelect one of the options or enter the {valor1} of RAM to assign to the server= ').replace(" ", "")
                    try:
                        if rammount.lower() == "m":
                            config()  
                        if rammount.lower() == "c":
                            if valor == "GB":
                                cls()
                                window_title(f'{SSTITLE} - RAM is now set to Megabytes')
                                day = getdate()
                                print(f"{SSTITLE} - {day}\n--------------------------\n\nRAM is now set to {gbormb}.")
                                time.sleep(1.5)
                                valor = "MB"
                                run_server()
                            elif valor == "MB":
                                cls()
                                window_title(f'{SSTITLE} - RAM is now set to Gigabytes')
                                day = getdate()
                                print(f"{SSTITLE} - {day}\n--------------------------\n\nRAM is now set to {gbormb}.")
                                time.sleep(1.5)
                                valor = "GB"
                                run_server()
                        elif rammount.lower() == "b":
                            ram()
                        elif rammount.lower() == "n":
                            eng()
                        else:
                            if any(char in "0123456789+-*/" for char in rammount):
                                if not rammount[0].isalpha():
                                    gbs = eval(rammount)
                                else:
                                    gbs = rammount
                            else:
                                gbs = rammount
                            gbs = int(gbs)
                            if valor == "GB" and (gbs <= 0 or gbs > 75):
                                cls()
                                window_title(f'{SSTITLE} - Invalid amount of RAM')
                                day = getdate()
                                print(f"{SSTITLE} - {day}\n--------------------------\n\nEnter a valid amount between 1 and 75 Gigabytes.")
                                time.sleep(1.5)
                                run_server()
                            elif valor == "MB" and (gbs <= 1023 or gbs > 76800):
                                cls()
                                window_title(f'{SSTITLE} - Invalid amount of RAM')
                                day = getdate()
                                print(f"{SSTITLE} - {day}\n--------------------------\n\nEnter a valid amount between 1,024 and 76,800 Megabytes.")
                                time.sleep(1.5)
                                run_server()
                            else:
                                with open("eula.txt", "w") as reemplazo:
                                    reemplazo.write("eula=true")
                                cls()
                                window_title(f'{SSTITLE} - Server running...')
                                day = getdate()
                                print(f"{SSTITLE} - {day}\n--------------------------\n\nStarting the server with {gbs}{valor} of RAM.\n")
                                comando_java = f"java -Xmx{gbs}{vjava} -Xms{gbs}{vjava} -jar server.jar nogui"
                                subprocess.run(comando_java, shell=True)
                                fyh_sistema = datetime.now()
                                fecha_cerrado = str(fyh_sistema.strftime("%d/%m/%Y"))
                                hora_cerrado = str(fyh_sistema.strftime("%H:%M:%S"))
                                input("\nPress ENTER to continue.")
                                cls()
                                window_title(f'{SSTITLE} - Server closed')
                                day = getdate()
                                input(f"{SSTITLE} - {day}\n--------------------------\n\nThe server has closed on {fecha_cerrado} at {hora_cerrado}.\n\nYou can check the console log in the 'logs' folder inside your Server's main folder.\n\nPress ENTER to continue.")
                                ram()
                    except (ValueError, SyntaxError, IndexError, ZeroDivisionError):
                        run_server()
                run_server()
            else:
                cls()
                window_title(f'{SSTITLE} - Server not found :(')
                day = getdate()
                print(f'{SSTITLE} - {day}\n--------------------------\n\n"server.jar" not found in this folder.\n\nAre you sure this is a Server?')
                time.sleep(2.5)
                ram()

        # INSTALL NEW SERVER
        def installmenu():
            LOGGER.info("Entering Server Installation menu...")
            global newserver
            global foldname
            cls()
            window_title(f'{SSTITLE} - Select a folder for the new server')
            day = getdate()
            inconfirm = input(f"{SSTITLE} - {day}\n--------------------------\n\nFirst, lets select a folder to save your New Server's files.\n\n(1) Select folder for the new Server\n(2) Cancel\n\nSelect one of the options= ").replace(" ", "")
            try:
                if any(char in "0123456789+-*/" for char in inconfirm):
                    if not inconfirm[0].isalpha():
                        inconf = eval(inconfirm)
                    else:
                        inconf = inconfirm
                else:
                    inconf = inconfirm
                inconf = int(inconf)
                if inconf == 1:
                    def reselect():
                        global newserver
                        global foldname
                        newserver = filedialog.askdirectory()
                        front()
                        foldname = colored(os.path.basename(newserver), "yellow") # type: ignore
                        if newserver == "" or foldname == "":
                            cls()
                            window_title(f'{SSTITLE} - You must select a folder')
                            day = getdate()
                            print(f'{SSTITLE} - {day}\n--------------------------\n\nYou must select a folder to save the New Server.')
                            time.sleep(2.5)
                            installmenu()
                        os.makedirs(newserver, exist_ok=True)
                        os.chdir(newserver)
                        if newserver and foldname:
                            def vers_select():
                                global newserver
                                global foldname
                                cls()
                                window_title(f'{SSTITLE} - Select version for your new server')
                                day = getdate()
                                verss = input(f'{SSTITLE} - {day}\n--------------------------\n\nYour New Server will be saved in "{foldname}".\n\n(L) See available versions\n(R) Re-select a folder for the New server\n(N) Return to main menu\n\nSelect one of the options or type the New Server version to install= ').replace(" ", "")
                                try:
                                    def servdownload(versionname,type):
                                        global newserver
                                        global foldname
                                        version = versionname.lower()
                                        if type == "stable":
                                            url = MC_STABLE[version]
                                        elif type == "snapshot":
                                            url = MC_SNAPSHOT[version]
                                        elif type == "aprils":
                                            url = MC_APRILS[version]
                                        elif type == "combat":
                                            url = MC_COMBAT[version]
                                        elif type == "old":
                                            url = MC_OLD[version]
                                        else:
                                            vers_select()
                                        cls()
                                        window_title(f'{SSTITLE} - Downloading server files...')
                                        day = getdate()
                                        print(f'{SSTITLE} - {day}\n--------------------------\n\nYour New Server is being downloaded.\n\nVersion: {version}\nTarget Folder: "{foldname}"\n\nPlease wait...\n')
                                        time.sleep(0.5)
                                        os.makedirs(newserver, exist_ok=True)
                                        os.chdir(newserver)
                                        try:
                                            response = requests.get(url, stream=True) # type: ignore
                                            total_size_in_bytes = int(response.headers.get('content-length', 0))
                                            block_size = 1024
                                            total_data = 0
                                            with open("server.jar", "wb") as file:
                                                for data in response.iter_content(block_size):
                                                    total_data += len(data)
                                                    file.write(data)
                                                    completed = int(50 * total_data / total_size_in_bytes)
                                                    print("\r[%s%s]" % ('#' * completed, '.' * (50 - completed)), end='')
                                            print()
                                            cls()
                                            window_title(f'{SSTITLE} - Server installed successfully')
                                            day = getdate()
                                            input(f'{SSTITLE} - {day}\n--------------------------\n\nThe server has been installed successfully and added to "Your Servers" list.\n\nPress ENTER to continue.')
                                            servname = os.path.basename(newserver)
                                            servstring = f"{servname}<[=]>{newserver}\n"
                                            os.makedirs(CONFIG_PATH, exist_ok=True)
                                            with open(SAVED_SERVERS, 'r+') as file:
                                                lines = file.readlines()
                                                if servstring not in lines:
                                                    file.write(servstring)
                                            eng()
                                        except Exception:
                                            def erragain():
                                                cls()
                                                yup = colored("Yes","green") # type: ignore
                                                nop = colored("No","red") # type: ignore
                                                window_title(f'{SSTITLE} - An error occurred while downloading the server :(')
                                                day = getdate()
                                                errtry = input(f"{SSTITLE} - {day}\n--------------------------\n\nAn error occurred while downloading your new server.\nTry again?\n\n(1) {yup}\n(2) {nop}\n\nSelect one of the options= ")
                                                try:
                                                    if any(char in "0123456789+-*/" for char in errtry):
                                                        if not errtry[0].isalpha():
                                                            errtr = eval(errtry)
                                                        else:
                                                            errtr = errtry
                                                    else:
                                                        errtr = errtry
                                                    errtr = int(errtr)
                                                    if errtr == 1:
                                                        servdownload(version,type)
                                                    elif errtr == 2:
                                                        eng()
                                                    else:
                                                        erragain()
                                                except (ValueError, SyntaxError, IndexError, ZeroDivisionError):
                                                    erragain()
                                                erragain()
                                    if verss.lower() == "n":
                                        eng()
                                    elif verss.lower() == "r":
                                        reselect()
                                    elif verss.lower() == "l":
                                        def select_list():
                                            cls()
                                            window_title(f'{SSTITLE} - List of available versions')
                                            day = getdate()
                                            print(f"{SSTITLE} - {day}\n--------------------------\n")
                                            print("STABLE VERSIONS:")
                                            for i, version in enumerate(MC_STABLE, start=1):
                                                print(f"(-) {version}")
                                            print('')
                                            print("SNAPSHOT VERSIONS:")
                                            for i, version in enumerate(MC_SNAPSHOT, start=1):
                                                print(f"(-) {version}")
                                            print('')
                                            print("APRIL'S FOOLS VERSIONS:")
                                            for i, version in enumerate(MC_APRILS, start=1):
                                                print(f"(-) {version}")
                                            print('')
                                            print("COMBAT TEST VERSIONS:")
                                            for i, version in enumerate(MC_COMBAT, start=1):
                                                print(f"(-) {version}")
                                            print('')
                                            print("OLD VERSIONS:")
                                            for i, version in enumerate(MC_OLD, start=1):
                                                print(f"(-) {version}")
                                            listselection = input("\n(B) Back\n(R) Return to main menu\n\nType a version to install or select one of the options=")
                                            try:
                                                if listselection.lower() == "b":
                                                    vers_select()
                                                elif listselection.lower() == "r":
                                                    eng()
                                                elif listselection.lower() in MC_STABLE.keys():
                                                    servdownload(listselection,"stable")
                                                elif listselection.lower() in MC_SNAPSHOT.keys():
                                                    servdownload(listselection,"snapshot")
                                                elif listselection.lower() in MC_APRILS.keys():
                                                    servdownload(listselection,"aprils")
                                                elif listselection.lower() in MC_COMBAT.keys():
                                                    servdownload(listselection,"combat")
                                                elif listselection.lower() in MC_OLD.keys():
                                                    servdownload(listselection,"old")
                                                else:
                                                    select_list()
                                            except (ValueError, SyntaxError, IndexError, ZeroDivisionError):
                                                select_list()
                                        select_list()
                                    elif verss.lower() in MC_STABLE.keys():
                                        servdownload(verss,"stable")
                                    elif verss.lower() in MC_SNAPSHOT.keys():
                                        servdownload(verss,"snapshot")
                                    elif verss.lower() in MC_APRILS.keys():
                                        servdownload(verss,"aprils")
                                    elif verss.lower() in MC_COMBAT.keys():
                                        servdownload(verss,"combat")
                                    elif verss.lower() in MC_OLD.keys():
                                        servdownload(verss,"old")
                                    else:
                                        vers_select()
                                except (ValueError, SyntaxError, IndexError, ZeroDivisionError):
                                    installmenu()
                            vers_select()
                        else:
                            installmenu()
                    reselect()
                elif inconf == 2:
                    eng()
                else:
                    installmenu()
            except (ValueError, SyntaxError, IndexError, ZeroDivisionError):
                installmenu()  

        # LICENSE AND EXTRAS
        def about():
            LOGGER.info("Entering Extras menu...")
            cls()
            window_title(f'{SSTITLE} - About {SSTITLE}')
            day = getdate()
            copyr = input(f"{SSTITLE} - {day}\n--------------------------\n\nMIT License - Copyright (c) {YEAR} ngdplnk\n\n{SSTITLE} {SSVERSION}\n\n{CHANGELOG_ENG}\n\n{HELPERS}\n\n-------------------------------------\n\n(1) View repository in the browser\n(2) View license in the browser\n(3) Return to main menu\n\nSelect one of the options= ")
            try:
                if any(char in "0123456789+-*/" for char in copyr):
                    if not copyr[0].isalpha():
                        selec = eval(copyr)
                    else:
                        selec = copyr
                else:
                    selec = copyr
                selec = int(selec)
                if selec == 1:
                    url = colored("https://github.com/ngdplnk/SSTools4MC","cyan") # type: ignore
                    cls()
                    window_title(f'{SSTITLE} - View repository')
                    day = getdate()
                    input(f"{SSTITLE} - {day}\n--------------------------\n\nThe repository will open in your browser.\n\n{url}\n\nPress ENTER to continue.")
                    url = "https://github.com/ngdplnk/SSTools4MC"
                    webbrowser.open(url)
                    about()
                elif selec == 2:
                    url = colored("https://github.com/ngdplnk/SSTools4MC/blob/main/LICENSE","cyan") # type: ignore
                    cls()
                    window_title(f'{SSTITLE} - View license')
                    day = getdate()
                    input(f"{SSTITLE} - {day}\n--------------------------\n\nThe license will open in your browser.\n\n{url}\n\nPress ENTER to continue.")
                    url = "https://github.com/ngdplnk/SSTools4MC/blob/main/LICENSE"
                    webbrowser.open(url)
                    about()
                elif selec == 3:
                    eng()
                else:
                    about()
            except (ValueError, SyntaxError, IndexError, ZeroDivisionError):
                about()

        # EXIT
        def exiit():
            cls()
            window_title(f'{SSTITLE} - See ya later!')
            print(f"--------------------------------------------\nSee ya later!\nMIT License - Copyright (c) {YEAR} ngdplnk\n--------------------------------------------\n")
            time.sleep(1.2)
            LOGGER.info("QUITTING PROGRAM...")
            sys.exit()

        # MAIN MENU
        def menu():
            LOGGER.info("Entering Main menu...")
            os.makedirs(SSTOOLS_FOLDER, exist_ok=True)
            os.chdir(SSTOOLS_FOLDER)
            cls()
            window_title(f'{SSTITLE} - Welcome! You are in the main menu')
            day = getdate()
            seleccion = input(f"{SSTITLE} - {day}\n--------------------------\n\nHi! You are in the main menu.\n\n(1) Start a Server\n(2) Install a New Server\n(3) Extras\n(4) Change Language\n(5) Exit\n\nSelect one of the options= ")
            try:
                if any(char in "0123456789+-*/" for char in seleccion):
                    if not seleccion[0].isalpha():
                        sel = eval(seleccion)
                    else:
                        sel = seleccion
                else:
                    sel = seleccion
                sel = int(sel)
                if sel == 1:
                    ram()
                elif sel == 2:
                    installmenu()
                elif sel == 3:
                    about()
                elif sel == 4:
                    esp()
                elif sel == 5:
                    exiit()
                menu()
            except (ValueError, SyntaxError, IndexError, ZeroDivisionError):
                menu()

        menu()

    # SPANISH
    def esp():
        # SERVER STARTUP
        def ram():
            LOGGER.info("Entering Server Startup menu...")
            global servername
            cls()
            sservers = {}
            if os.path.exists(SAVED_SERVERS):
                with open(SAVED_SERVERS, 'r') as file:
                    for line in file:
                        line = line.strip()
                        if line and not line.startswith('#'):
                            key, value = line.split('<[=]>')
                            sservers[key.strip()] = value.strip()
                if sservers:
                    cls()
                    window_title(f'{SSTITLE} - Lista "Tus Servidores"')
                    day = getdate()
                    print(f'{SSTITLE} - {day}\n--------------------------\n\nLista "Tus Servidores"\n')
                    server_keys = list(sservers.keys())
                    for i, key in enumerate(server_keys, start=1):
                        print(f"({i}) {key}")
                    nserv = colored("Añadir","cyan") # type: ignore
                    delserv = colored("Eliminar","red") # type: ignore
                    clearlist = colored("Limpiar","magenta") # type: ignore
                    print(f"\n(N) {nserv} Servidor\n(D) {delserv} un Servidor de la Lista\n(C) {clearlist} Lista\n(R) Volver al menú principal")
                    servsel = input("\nElige una de las opciones o escribe el número del Servidor que iniciarás= ").replace(" ", "")
                    try:
                        if servsel.lower() == "n":
                            newserv = filedialog.askdirectory()
                            front()
                            servname = os.path.basename(newserv)
                            server_jar_path = os.path.join(newserv, "server.jar")
                            if newserv == "" or servname == "":
                                newserv = False
                                servname = False
                            if newserv and servname and os.path.isfile(server_jar_path):
                                servname = colored(servname, "yellow") # type: ignore
                                with open(SAVED_SERVERS, 'r') as file:
                                    lines = file.readlines()
                                    servstring = f"{servname}<[=]>{newserv}\n"
                                    if servstring not in lines:
                                        os.makedirs(CONFIG_PATH, exist_ok=True)
                                        with open(SAVED_SERVERS, 'r+') as file:
                                            file.write(servstring)
                            else:
                                cls()
                                window_title(f'{SSTITLE} - Debes seleccionar una carpeta válida con un servidor')
                                day = getdate()
                                print(f'{SSTITLE} - {day}\n--------------------------\n\nDebes seleccionar una carpeta válida con un servidor para guardarla en la Lista "Tus Servidores".')
                                time.sleep(2.5)
                                ram()
                            cls()
                            window_title(f'{SSTITLE} - Servidor guardado')
                            day = getdate()
                            print(f'{SSTITLE} - {day}\n--------------------------\n\nEl servidor "{servname}" ha sido guardado.')
                            time.sleep(1.5)
                            ram()
                        elif servsel.lower() == "d":
                            def servdel():
                                cls()
                                window_title(f'{SSTITLE} - Eliminar un servidor')
                                day = getdate()
                                print(f"{SSTITLE} - {day}\n--------------------------\n\nSelecciona el Servidor que eliminarás de la lista.\n")
                                for i, key in enumerate(server_keys, start=1):
                                    print(f"({i}) {key}")
                                print("\n(N) Cancelar\n(R) Volver al menú principal")
                                servsel = input("\nSelecciona una de las opciones o ingresa el número del Servidor que eliminarás de la lista= ").replace(" ", "")
                                try:
                                    if servsel.lower() == "r":
                                        esp()
                                    elif servsel.lower() == "n":
                                        ram()
                                    else:
                                        if any(char in "0123456789+-*/" for char in servsel):
                                            if not servsel[0].isalpha():
                                                servv = eval(servsel)
                                            else:
                                                servv = servsel
                                        else:
                                            servv = servsel
                                        servsel = int(servv)
                                        if 1 <= servsel <= len(server_keys):
                                            servsel = server_keys[servsel - 1]
                                            servpath = sservers[servsel]
                                            servestring = f"{servsel}<[=]>{servpath}\n"
                                        os.makedirs(CONFIG_PATH, exist_ok=True)
                                        with open(SAVED_SERVERS, 'r') as file:
                                            lines = file.readlines()
                                            os.makedirs(CONFIG_PATH, exist_ok=True)
                                            with open(SAVED_SERVERS, 'w') as file:
                                                for line in lines:
                                                    if line != servestring:
                                                        file.write(line)
                                        cls()
                                        window_title(f'{SSTITLE} - Servidor eliminado')
                                        day = getdate()
                                        print(f'{SSTITLE} - {day}\n--------------------------\n\nEl Servidor "{servsel}" ha sido eliminado de la lista.')
                                        time.sleep(1.5)
                                        ram()             
                                except (ValueError, SyntaxError, IndexError, ZeroDivisionError):
                                    servdel()
                            servdel()
                        elif servsel.lower() == "c":
                            def lisclear():
                                cls()
                                yess = colored("Sí","green") # type: ignore
                                noo = colored("No","red") # type: ignore
                                window_title(f'{SSTITLE} - Estás seguro?')
                                day = getdate()
                                clearconfirm = input(f'{SSTITLE} - {day}\n--------------------------\n\nEstás seguro de que quieres limpiar la Lista "Tus Servidores"?\n\n(1) {yess}\n(2) {noo}\n\nElige una de las opciones= ')
                                try:
                                    if any(char in "0123456789+-*/" for char in clearconfirm):
                                        if not clearconfirm[0].isalpha():
                                            clearconf = eval(clearconfirm)
                                        else:
                                            clearconf = clearconfirm
                                    else:
                                        clearconf = clearconfirm
                                    clearconf = int(clearconf)
                                    if clearconf == 1:
                                        os.makedirs(CONFIG_PATH, exist_ok=True)
                                        with open(SAVED_SERVERS, 'w') as file:
                                            file.write("# SSTools4MC\n# Servidores guardados\n")
                                        cls()
                                        window_title(f'{SSTITLE} - Lista limpiada')
                                        print(f'{SSTITLE} - {day}\n--------------------------\n\nLa Lista "Tus Servidores" ha sido limpiada.')
                                        time.sleep(1.5)
                                        ram()
                                    elif clearconf == 2:
                                        ram()
                                except (ValueError, SyntaxError, IndexError, ZeroDivisionError):
                                    lisclear()
                            lisclear()
                        elif servsel.lower() == "r":
                            esp()
                        else:
                            if any(char in "0123456789+-*/" for char in servsel):
                                if not servsel[0].isalpha():
                                    servv = eval(servsel)
                                else:
                                    servv = servsel
                            else:
                                servv = servsel
                            servsel = int(servv)
                            if 1 <= servsel <= len(server_keys):
                                servsel = server_keys[servsel - 1]
                                servpath = sservers[servsel]
                                os.makedirs(servpath, exist_ok=True)
                                os.chdir(servpath)
                                servername = servsel
                    except (ValueError, SyntaxError, IndexError, ZeroDivisionError):
                        ram()
                else:
                    os.makedirs(CONFIG_PATH, exist_ok=True)
                    with open(SAVED_SERVERS, 'w') as file:
                        file.write("# SSTools4MC\n# Servidores Guardados\n")
                    cls()
                    adds = colored("Añadir un Servidor","cyan") # type: ignore
                    window_title(f'{SSTITLE} - No hay servidores guardados')
                    day = getdate()
                    saveconfirm = input(f"{SSTITLE} - {day}\n--------------------------\n\nNo tienes ningún Servidor guardado.\n\n(1) {adds}\n(2) Volver al menú principal\n\nElige una de las opciones= ")
                    try:
                        if any(char in "0123456789+-*/" for char in saveconfirm):
                            if not saveconfirm[0].isalpha():
                                saveconf = eval(saveconfirm)
                            else:
                                saveconf = saveconfirm
                        else:
                            saveconf = saveconfirm
                        saveconf = int(saveconf)
                        if saveconf == 1:
                            newserv = filedialog.askdirectory()
                            front()
                            servname = os.path.basename(newserv)
                            server_jar_path = os.path.join(newserv, "server.jar")
                            if newserv == "" or servname == "":
                                newserv = False
                                servname = False
                            if newserv and servname and os.path.isfile(server_jar_path):
                                servname = colored(servname, "yellow") # type: ignore
                                with open(SAVED_SERVERS, 'r') as file:
                                    lines = file.readlines()
                                    servstring = f"{servname}<[=]>{newserv}\n"
                                    if servstring not in lines:
                                        os.makedirs(CONFIG_PATH, exist_ok=True)
                                        with open(SAVED_SERVERS, 'r+') as file:
                                            file.write(servstring)
                            else:
                                cls()
                                window_title(f'{SSTITLE} - Debes seleccionar una carpeta válida con un servidor')
                                day = getdate()
                                print(f'{SSTITLE} - {day}\n--------------------------\n\nDebes seleccionar una carpeta válida con un servidor para guardarla en la Lista "Tus Servidores".')
                                time.sleep(2.5)
                                ram()
                            cls()
                            window_title(f'{SSTITLE} - Servidor guardado')
                            day = getdate()
                            print(f'{SSTITLE} - {day}\n--------------------------\n\nEl Servidor "{servname}" ha sido guardado.')
                            time.sleep(1.5)
                            ram()
                        elif saveconf == 2:
                            esp()
                        else:
                            ram()
                    except (ValueError, SyntaxError, IndexError, ZeroDivisionError):
                        ram()
            else:
                os.makedirs(CONFIG_PATH, exist_ok=True)
                with open(SAVED_SERVERS, 'w') as file:
                    file.write("# SSTools4MC\n# Servidores Guardados\n")
                cls()
                window_title(f'{SSTITLE} - No hay servidores guardados')
                day = getdate()
                input(f'{SSTITLE} - {day}\n--------------------------\n\nNo tienes ningún Servidor guardado.\n\nPresiona ENTER para seleccionar una carpeta con un Servidor y guardarlo en la Lista "Tus Servidores".')
                newserv = filedialog.askdirectory()
                front()
                servname = os.path.basename(newserv)
                server_jar_path = os.path.join(newserv, "server.jar")
                if newserv == "" or servname == "":
                    newserv = False
                    servname = False
                if newserv and servname and os.path.isfile(server_jar_path):
                    servname = colored(servname, "yellow") # type: ignore
                    with open(SAVED_SERVERS, 'r') as file:
                        lines = file.readlines()
                        servstring = f"{servname}<[=]>{newserv}\n"
                        if servstring not in lines:
                            os.makedirs(CONFIG_PATH, exist_ok=True)
                            with open(SAVED_SERVERS, 'r+') as file:
                                file.write(servstring)
                else:
                    cls()
                    window_title(f'{SSTITLE} - Debes seleccionar una carpeta válida con un servidor')
                    day = getdate()
                    print(f'{SSTITLE} - {day}\n--------------------------\n\nDebes seleccionar una carpeta válida con un servidor para guardarla en la Lista "Tus Servidores".')
                    time.sleep(2.5)
                    ram()
                cls()
                window_title(f'{SSTITLE} - Servidor guardado')
                day = getdate()
                print(f'{SSTITLE} - {day}\n--------------------------\n\nEl Servidor "{servname}" ha sido guardado.')
                time.sleep(1.5)
                ram()
            if os.path.exists("server.jar"):
                # CONFIG
                def config():
                    global nameserver
                    cls()
                    props = "server.properties"
                    if os.path.exists(props):
                        global properties
                        properties = {}
                        online = "Error"
                        hard = "Error"
                        pvp = "Error"
                        with open('server.properties', 'r') as file:
                            for line in file:
                                line = line.strip()
                                if line and not line.startswith('#'):
                                    key, value = line.split('=')
                                    properties[key.strip()] = value.strip()
                        if properties["online-mode"] == "false":
                            online = colored("ACTIVAR","green") # type: ignore
                        elif properties["online-mode"] == "true":
                            online = colored("DESACTIVAR","red") # type: ignore
                        if properties["hardcore"] == "false":
                            hard = colored("ACTIVAR","green") # type: ignore
                        elif properties["hardcore"] == "true":
                            hard = colored("DESACTIVAR","red") # type: ignore
                        if properties["pvp"] == "false":
                            pvp = colored("ACTIVAR","green") # type: ignore
                        elif properties["pvp"] == "true":
                            pvp = colored("DESACTIVAR","red") # type: ignore
                        cls()
                        window_title(f'{SSTITLE} - Gestión del servidor')
                        day = getdate()
                        confsel = input(f'{SSTITLE} - {day}\n--------------------------\n\nConfiguremos "{nameserver}"!\n\n(1) {online} modo online\n(2) {hard} modo extremo\n(3) {pvp} PvP\n(4) Cambiar modo de juego\n(5) Cambiar dificultad\n(6) Cambiar el límite de jugadores\n(7) Atrás\n(8) Volver al menú principal\n\nElige una de las opciones= ')
                        if properties["online-mode"] == "false":
                            online = "ENABLE"
                        elif properties["online-mode"] == "true":
                            online = "DISABLE"
                        if properties["hardcore"] == "false":
                            hard = "ENABLE"
                        elif properties["hardcore"] == "true":
                            hard = "DISABLE"
                        if properties["pvp"] == "false":
                            pvp = "ENABLE"
                        elif properties["pvp"] == "true":
                            pvp = "DISABLE"
                        try:
                            if any(char in "0123456789+-*/" for char in confsel):
                                if not confsel[0].isalpha():
                                    confug = eval(confsel)
                                else:
                                    confug = confsel
                            else:
                                confug = confsel
                            confug = int(confug) 
                            if confug == 1:
                                if online == "ENABLE":
                                    properties["online-mode"] = "true"
                                    with open('server.properties', 'w') as file:
                                        for key, value in properties.items():
                                            file.write(f'{key}={value}\n')
                                    online = colored("ACTIVADO","green") # type: ignore
                                elif online == "DISABLE":
                                    properties["online-mode"] = "false"
                                    with open('server.properties', 'w') as file:
                                        for key, value in properties.items():
                                            file.write(f'{key}={value}\n')
                                    online = colored("DESACTIVADO","red") # type: ignore
                                cls()
                                window_title(f'{SSTITLE} - Modo online alternado')
                                day = getdate()
                                print(f"{SSTITLE} - {day}\n--------------------------\n\nEl modo online se ha {online}.")
                                time.sleep(1.5)
                                config()
                            elif confug == 2:
                                if hard == "ENABLE":
                                    properties["hardcore"] = "true"
                                    with open('server.properties', 'w') as file:
                                        for key, value in properties.items():
                                            file.write(f'{key}={value}\n')
                                    hard = colored("ACTIVADO","green") # type: ignore
                                elif hard == "DISABLE":
                                    properties["hardcore"] = "false"
                                    with open('server.properties', 'w') as file:
                                        for key, value in properties.items():
                                            file.write(f'{key}={value}\n')
                                    hard = colored("DESACTIVADO","red") # type: ignore
                                cls()
                                window_title(f'{SSTITLE} - Modo extremo alternado')
                                day = getdate()
                                print(f"{SSTITLE} - {day}\n--------------------------\n\nEl modo extremo se ha {hard}.")
                                time.sleep(1.5)
                                config()
                            elif confug == 3:
                                if pvp == "ENABLE":
                                    properties["pvp"] = "true"
                                    with open('server.properties', 'w') as file:
                                        for key, value in properties.items():
                                            file.write(f'{key}={value}\n')
                                    pvp = colored("ACTIVADO","green") # type: ignore
                                elif pvp == "DISABLE":
                                    properties["pvp"] = "false"
                                    with open('server.properties', 'w') as file:
                                        for key, value in properties.items():
                                            file.write(f'{key}={value}\n')
                                    pvp = colored("DESACTIVADO","red") # type: ignore
                                cls()
                                window_title(f'{SSTITLE} - PvP alternado')
                                day = getdate()
                                print(f"{SSTITLE} - {day}\n--------------------------\n\nEl PvP se ha {pvp}.")
                                time.sleep(1.5)
                                config()
                            elif confug == 4:
                                def juego():
                                    global properties
                                    modo = properties["gamemode"]
                                    if modo == "survival" or modo == "0":
                                        modo = colored("SUPERVIVENCIA","cyan") # type: ignore
                                    elif modo == "creative" or modo == "1":
                                        modo = colored("CREATIVO","cyan") # type: ignore
                                    elif modo == "adventure" or modo == "2":
                                        modo = colored("AVENTURA","cyan") # type: ignore
                                    elif modo == "spectator" or modo == "3":
                                        modo = colored("ESPECTADOR","cyan") # type: ignore
                                    superv = colored("SUPERVIVENCIA","yellow") # type: ignore
                                    creat = colored("CREATIVO","yellow") # type: ignore
                                    avent = colored("AVENTURA","yellow") # type: ignore
                                    espect = colored("ESPECTADOR","yellow") # type: ignore
                                    cls()
                                    window_title(f'{SSTITLE} - Configuración de modo de juego')
                                    day = getdate()
                                    modosel = input(f"{SSTITLE} - {day}\n--------------------------\n\nEl modo de juego actual es {modo}.\n\n(1) Cambiar a modo {superv}\n(2) Cambiar a modo {creat}\n(3) Cambiar a modo {avent}\n(4) Cambiar a modo {espect}\n(5) Atrás\n(6) Volver al menú principal\n\nElige una de las opciones= ")
                                    try:
                                        if any(char in "0123456789+-*/" for char in modosel):
                                            if not modosel[0].isalpha():
                                                coonf = eval(modosel)
                                            else:
                                                coonf = modosel
                                        else:
                                            coonf = modosel
                                        coonf = int(coonf)
                                        if coonf == 1:
                                            properties["gamemode"] = "0"
                                            with open('server.properties', 'w') as file:
                                                for key, value in properties.items():
                                                    file.write(f'{key}={value}\n')
                                            cls()
                                            window_title(f'{SSTITLE} - El modo de juego ahora es Supervivencia')
                                            day = getdate()
                                            print(f"{SSTITLE} - {day}\n--------------------------\n\nEl modo de juego ahora es {superv}.")
                                            time.sleep(1.5)
                                            juego()
                                        elif coonf == 2:
                                            properties["gamemode"] = "1"
                                            with open('server.properties', 'w') as file:
                                                for key, value in properties.items():
                                                    file.write(f'{key}={value}\n')
                                            cls()
                                            window_title(f'{SSTITLE} - El modo de juego ahora es Creativo')
                                            day = getdate()
                                            print(f"{SSTITLE} - {day}\n--------------------------\n\nEl modo de juego ahora es {creat}.")
                                            time.sleep(1.5)
                                            juego()
                                        elif coonf == 3:
                                            properties["gamemode"] = "2"
                                            with open('server.properties', 'w') as file:
                                                for key, value in properties.items():
                                                    file.write(f'{key}={value}\n')
                                            cls()
                                            window_title(f'{SSTITLE} - El modo de juego ahora es Aventura')
                                            day = getdate()
                                            print(f"{SSTITLE} - {day}\n--------------------------\n\nEl modo de juego ahora es {avent}.")
                                            time.sleep(1.5)
                                            juego()
                                        elif coonf == 4:
                                            properties["gamemode"] = "3"
                                            with open('server.properties', 'w') as file:
                                                for key, value in properties.items():
                                                    file.write(f'{key}={value}\n')
                                            cls()
                                            window_title(f'{SSTITLE} - El modo de juego ahora es Espectador')
                                            day = getdate()
                                            print(f"{SSTITLE} - {day}\n--------------------------\n\nEl modo de juego ahora es {espect}.")
                                            time.sleep(1.5)
                                            juego()
                                        elif coonf == 5:
                                            config()
                                        elif coonf == 6:
                                            esp()
                                        else:
                                            juego()
                                    except (ValueError, SyntaxError, IndexError, ZeroDivisionError):
                                        juego()
                                juego()
                            elif confug == 5:
                                def difconf():
                                    global properties
                                    dificultad = properties["difficulty"]
                                    if dificultad == "peaceful" or dificultad == "0":
                                        dificultad = colored("PACÍFICO","cyan") # type: ignore
                                    elif dificultad == "easy" or dificultad == "1":
                                        dificultad = colored("FÁCIL","cyan") # type: ignore
                                    elif dificultad == "normal" or dificultad == "2":
                                        dificultad = colored("NORMAL","cyan") # type: ignore
                                    elif dificultad == "hard" or dificultad == "3":
                                        dificultad = colored("DIFÍCIL","cyan") # type: ignore
                                    pacif = colored("PACÍFICO","yellow") # type: ignore
                                    facil = colored("FÁCIL","yellow") # type: ignore
                                    normal = colored("NORMAL","yellow") # type: ignore
                                    dificil = colored("DIFÍCIL","yellow") # type: ignore
                                    cls()
                                    window_title(f'{SSTITLE} - Configuración de dificultad')
                                    day = getdate()
                                    difsel = input(f"{SSTITLE} - {day}\n--------------------------\n\nLa dificultad actual es {dificultad}.\n\n(1) Cambiar a dificultad {pacif}\n(2) Cambiar a dificultad {facil}\n(3) Cambiar a dificultad {normal}\n(4) Cambiar a dificultad {dificil}\n(5) Atrás\n(6) Volver al menú principal\n\nElige una de las opciones= ")
                                    try:
                                        if any(char in "0123456789+-*/" for char in difsel):
                                            if not difsel[0].isalpha():
                                                difcc = eval(difsel)
                                            else:
                                                difcc = difsel
                                        else:
                                            difcc = difsel
                                        difcc = int(difcc)
                                        if difcc == 1:
                                            properties["difficulty"] = "0"
                                            with open('server.properties', 'w') as file:
                                                for key, value in properties.items():
                                                    file.write(f'{key}={value}\n')
                                            cls()
                                            window_title(f'{SSTITLE} - La dificultad ahora es Pacífico')
                                            day = getdate()
                                            print(f"{SSTITLE} - {day}\n--------------------------\n\nLa dificultad ahora es {pacif}.")
                                            time.sleep(1.5)
                                            difconf()
                                        elif difcc == 2:
                                            properties["difficulty"] = "1"
                                            with open('server.properties', 'w') as file:
                                                for key, value in properties.items():
                                                    file.write(f'{key}={value}\n')
                                            cls()
                                            window_title(f'{SSTITLE} - La dificultad ahora es Fácil')
                                            day = getdate()
                                            print(f"{SSTITLE} - {day}\n--------------------------\n\nLa dificultad ahora es {facil}.")
                                            time.sleep(1.5)
                                            difconf()
                                        elif difcc == 3:
                                            properties["difficulty"] = "2"
                                            with open('server.properties', 'w') as file:
                                                for key, value in properties.items():
                                                    file.write(f'{key}={value}\n')
                                            cls()
                                            window_title(f'{SSTITLE} - La dificultad ahora es Normal')
                                            day = getdate()
                                            print(f"{SSTITLE} - {day}\n--------------------------\n\nLa dificultad ahora es {normal}.")
                                            time.sleep(1.5)
                                            difconf()
                                        elif difcc == 4:
                                            properties["difficulty"] = "3"
                                            with open('server.properties', 'w') as file:
                                                for key, value in properties.items():
                                                    file.write(f'{key}={value}\n')
                                            cls()
                                            window_title(f'{SSTITLE} - La dificultad ahora es Difícil')
                                            day = getdate()
                                            print(f"{SSTITLE} - {day}\n--------------------------\n\nLa dificultad ahora es {dificil}.")
                                            time.sleep(1.5)
                                            difconf()
                                        elif difcc == 5:
                                            config()
                                        elif difcc == 6:
                                            esp()
                                        else:
                                            difconf()
                                    except (ValueError, SyntaxError, IndexError, ZeroDivisionError):
                                        difconf()
                                difconf()
                            elif confug == 6:
                                def playct():
                                    global properties
                                    players = colored(properties["max-players"],"cyan") # type: ignore
                                    cls()
                                    window_title(f'{SSTITLE} - Configuración de límite de jugadores')
                                    day = getdate()
                                    newpl = input(f"{SSTITLE} - {day}\n--------------------------\n\nEl límite de jugadores actual es de {players} jugadores.\n\n(N) Atrás\n(M) Volver al menú principal\n\nElige una de las opciones o ingresa el nuevo límite de jugadores= ").replace(" ", "")
                                    try:
                                        if newpl.lower() == "n":
                                            config()
                                        elif newpl.lower() == "m":
                                            esp()
                                        else:
                                            if any(char in "0123456789+-*/" for char in newpl):
                                                if not newpl[0].isalpha():
                                                    entero = eval(newpl)
                                                else:
                                                    entero = newpl
                                            else:
                                                entero = newpl
                                            entero = int(entero)
                                            if entero <= 0 or entero > 100000:
                                                cls()
                                                window_title(f'{SSTITLE} - Cantidad de límite de jugadores inválida')
                                                day = getdate()
                                                print(f"{SSTITLE} - {day}\n--------------------------\n\nIngresa un número válido entre 1 y 100.000.")
                                                time.sleep(1.5)
                                                playct()
                                            else:
                                                properties["max-players"] = entero
                                                with open('server.properties', 'w') as file:
                                                    for key, value in properties.items():
                                                        file.write(f'{key}={value}\n')
                                                entero = colored(str(entero),"yellow") # type: ignore
                                                cls()
                                                window_title(f'{SSTITLE} - Límite de jugadores cambiado')
                                                day = getdate()
                                                print(f"{SSTITLE} - {day}\n--------------------------\n\nEl límite de jugadores ahora es {entero}.")
                                                time.sleep(1.5)
                                                playct()
                                    except (ValueError, SyntaxError, IndexError, ZeroDivisionError):
                                        playct()
                                playct()
                            elif confug == 7:
                                run_server()
                            elif confug == 8:
                                esp()
                            else:
                                config()
                        except (ValueError, SyntaxError, IndexError, ZeroDivisionError):
                            config()
                    else:
                        cls()
                        window_title(f'{SSTITLE} - Archivos de configuración del servidor no encontrados :(')
                        day = getdate()
                        input(f"{SSTITLE} - {day}\n--------------------------\n\nLos achivos de configuración del Servidor aún no existen o no están disponibles.\nDebes iniciar el Servidor correctamente al menos 1 vez antes de poder configurarlo.\n\nPresiona ENTER para continuar.")
                        run_server()
                def run_server():
                    global servername
                    global valor
                    global nameserver
                    valor1 = None
                    gbormb = None
                    vjava = None
                    if valor == None:
                        valor = "GB"
                        valor1 = colored("GIGABYTES","cyan") # type: ignore
                        vjava = "G"
                        gbormb = colored("MEGABYTES","yellow") # type: ignore
                    if valor == "GB":
                        valor1 = colored("GIGABYTES","cyan") # type: ignore
                        vjava = "G"
                        gbormb = colored("MEGABYTES","yellow") # type: ignore
                    elif valor == "MB":
                        valor1 = colored("MEGABYTES","cyan") # type: ignore
                        vjava = "M"
                        gbormb = colored("GIGABYTES","yellow") # type: ignore
                    nameserver = servername
                    cls()
                    gbs = 0
                    window_title(f'{SSTITLE} - Estás a punto de iniciar el servidor!')
                    day = getdate()
                    rammount = input(f'{SSTITLE} - {day}\n--------------------------\n\nEstás a punto de iniciar el Servidor "{nameserver}"\n\n(M) Configurar Servidor\n(C) Usar RAM en {gbormb}\n(B) Atrás\n(N) Volver al menú principal\n\nElige una de las opciones o ingresa los {valor1} de RAM para asignar a tu Servidor= ').replace(" ", "")
                    try:
                        if rammount.lower() == "m":
                            config()  
                        if rammount.lower() == "c":
                            if valor == "GB":
                                cls()
                                window_title(f'{SSTITLE} - La RAM ahora está en Megabytes')
                                day = getdate()
                                print(f"{SSTITLE} - {day}\n--------------------------\n\nLa RAM ahora está en {gbormb}.")
                                time.sleep(1.5)
                                valor = "MB"
                                run_server()
                            elif valor == "MB":
                                cls()
                                window_title(f'{SSTITLE} - La RAM ahora está en Gigabytes')
                                day = getdate()
                                print(f"{SSTITLE} - {day}\n--------------------------\n\nLa RAM ahora está en {gbormb}.")
                                time.sleep(1.5)
                                valor = "GB"
                                run_server()
                        elif rammount.lower() == "b":
                            ram()
                        elif rammount.lower() == "n":
                            esp()
                        else:
                            if any(char in "0123456789+-*/" for char in rammount):
                                if not rammount[0].isalpha():
                                    gbs = eval(rammount)
                                else:
                                    gbs = rammount
                            else:
                                gbs = rammount
                            gbs = int(gbs)
                            if valor == "GB" and (gbs <= 0 or gbs > 75):
                                cls()
                                window_title(f'{SSTITLE} - Cantidad de RAM inválida')
                                day = getdate()
                                print(f"{SSTITLE} - {day}\n--------------------------\n\nIngresa una cantidad válida entre 1 y 75 Gigabytes.")
                                time.sleep(1.5)
                                run_server()
                            elif valor == "MB" and (gbs <= 1023 or gbs > 76800):
                                cls()
                                window_title(f'{SSTITLE} - Cantidad de RAM inválida')
                                day = getdate()
                                print(f"{SSTITLE} - {day}\n--------------------------\n\nIngresa una cantidad válida entre 1.024 y 76.800 Megabytes.")
                                time.sleep(1.5)
                                run_server()
                            else:
                                with open('eula.txt', "w") as reemplazo:
                                    reemplazo.write("eula=true")
                                cls()
                                window_title(f'{SSTITLE} - Servidor corriendo...')
                                day = getdate()
                                print(f"{SSTITLE} - {day}\n--------------------------\n\nIniciando el Servidor con {gbs}{valor} de RAM.\n")
                                comando_java = f"java -Xmx{gbs}{vjava} -Xms{gbs}{vjava} -jar server.jar nogui"
                                subprocess.run(comando_java, shell=True)
                                fyh_sistema = datetime.now()
                                fecha_cerrado = str(fyh_sistema.strftime("%d/%m/%Y"))
                                hora_cerrado = str(fyh_sistema.strftime("%H:%M:%S"))
                                input("\nPresiona ENTER para continuar.")
                                cls()
                                window_title(f'{SSTITLE} - Servidor cerrado')
                                day = getdate()
                                input(f"{SSTITLE} - {day}\n--------------------------\n\nEl Servidor se ha cerrado el {fecha_cerrado} a las {hora_cerrado}.\n\nPuedes ver el registro de la consola en la carpeta 'logs' dentro de la carpeta principal de tu Servidor.\n\nPresiona ENTER para continuar.")
                                ram()
                    except (ValueError, SyntaxError, IndexError, ZeroDivisionError):
                        run_server()
                run_server()
            else:
                cls()
                window_title(f'{SSTITLE} - No se encuentra el servidor :(')
                day = getdate()
                print(f'{SSTITLE} - {day}\n--------------------------\n\nNo se encuentra "server.jar" en esta carpeta.\n\nEstás seguro que esto es un Servidor?')
                time.sleep(2.5)
                ram()

        # INSTALL NEW SERVER
        def installmenu():
            LOGGER.info("Entering Server Installation menu...")
            global newserver
            global foldname
            cls()
            window_title(f'{SSTITLE} - Instalar un nuevo servidor')
            day = getdate()
            inconfirm = input(f"{SSTITLE} - {day}\n--------------------------\n\nPrimero, seleccionemos una carpeta para guardar los archivos de tu Nuevo Servidor.\n\n(1) Seleccionar una carpeta para el Nuevo Servidor\n(2) Cancelar\n\nElige una de las opciones= ").replace(" ", "")
            try:
                if any(char in "0123456789+-*/" for char in inconfirm):
                    if not inconfirm[0].isalpha():
                        inconf = eval(inconfirm)
                    else:
                        inconf = inconfirm
                else:
                    inconf = inconfirm
                inconf = int(inconf)
                if inconf == 1:
                    def reselect():
                        global newserver
                        global foldname
                        newserver = filedialog.askdirectory()
                        front()
                        foldname = colored(os.path.basename(newserver), "yellow") # type: ignore
                        if newserver == "" or foldname == "":
                            cls()
                            window_title(f'{SSTITLE} - Debes seleccionar una carpeta')
                            day = getdate()
                            print(f'{SSTITLE} - {day}\n--------------------------\n\nDebes elegir una carpeta para guardar tu Nuevo Servidor.')
                            time.sleep(2.5)
                            installmenu()
                        os.makedirs(newserver, exist_ok=True)
                        os.chdir(newserver)
                        if newserver and foldname:
                            def vers_select():
                                global newserver
                                global foldname
                                cls()
                                window_title(f'{SSTITLE} - Seleccionar versión para tu nuevo servidor')
                                day = getdate()
                                verss = input(f'{SSTITLE} - {day}\n--------------------------\n\nTu Nuevo Servidor se guardará en "{foldname}".\n\n(L) Ver versiones disponibles\n(R) Reelegir una carpeta para el Nuevo Servidor\n(N) Volver al menú principal\n\nElige una de las opciones o escribe la versión para instalar tu Nuevo Servidor= ').replace(" ", "")
                                try:
                                    def servdownload(versionname,type):
                                        global newserver
                                        global foldname
                                        version = versionname.lower()
                                        if type == "stable":
                                            url = MC_STABLE[version]
                                        elif type == "snapshot":
                                            url = MC_SNAPSHOT[version]
                                        elif type == "aprils":
                                            url = MC_APRILS[version]
                                        elif type == "combat":
                                            url = MC_COMBAT[version]
                                        elif type == "old":
                                            url = MC_OLD[version]
                                        else:
                                            vers_select()
                                        cls()
                                        window_title(f'{SSTITLE} - Descargando archivos del servidor...')
                                        day = getdate()
                                        print(f'{SSTITLE} - {day}\n--------------------------\n\nTu Nuevo Servidor está siendo descargado.\n\nVersión: {version}\nCarpeta de destino: "{foldname}"\n\nEspera por favor...\n')
                                        time.sleep(0.5)
                                        os.makedirs(newserver, exist_ok=True)
                                        os.chdir(newserver)
                                        try:
                                            response = requests.get(url, stream=True) # type: ignore
                                            total_size_in_bytes = int(response.headers.get('content-length', 0))
                                            block_size = 1024  # 1 Kibibyte
                                            total_data = 0
                                            with open("server.jar", "wb") as file:
                                                for data in response.iter_content(block_size):
                                                    total_data += len(data)
                                                    file.write(data)
                                                    completed = int(50 * total_data / total_size_in_bytes)
                                                    print("\r[%s%s]" % ('#' * completed, '.' * (50 - completed)), end='')
                                            print()
                                            cls()
                                            window_title(f'{SSTITLE} - Tu nuevo servidor ha sido instalado correctamente')
                                            day = getdate()
                                            input(f'{SSTITLE} - {day}\n--------------------------\n\nTu Nuevo Servidor se ha instalado correctamente y ha sido añadido a la Lista "Tus Servidores".\n\nPresiona ENTER para continuar.')
                                            servname = os.path.basename(newserver)
                                            servstring = f"{servname}<[=]>{newserver}\n"
                                            os.makedirs(CONFIG_PATH, exist_ok=True)
                                            with open(SAVED_SERVERS, 'r+') as file:
                                                lines = file.readlines()
                                                if servstring not in lines:
                                                    file.write(servstring)
                                            esp()
                                        except Exception:
                                            def erragain():
                                                cls()
                                                yup = colored("Sí","green") # type: ignore
                                                nop = colored("No","red") # type: ignore
                                                window_title(f'{SSTITLE} - Ocurrió un error mientras se descargaba tu nuevo servidor :(')
                                                day = getdate()
                                                errtry = input(f"{SSTITLE} - {day}\n--------------------------\n\nOcurrió un error mientras se descargaba tu Nuevo Servidor.\nReintentar?\n\n(1) {yup}\n(2) {nop}\n\nElige una de las opciones= ")
                                                try:
                                                    if any(char in "0123456789+-*/" for char in errtry):
                                                        if not errtry[0].isalpha():
                                                            errtr = eval(errtry)
                                                        else:
                                                            errtr = errtry
                                                    else:
                                                        errtr = errtry
                                                    errtr = int(errtr)
                                                    if errtr == 1:
                                                        servdownload(version,type)
                                                    elif errtr == 2:
                                                        esp()
                                                    else:
                                                        erragain()
                                                except (ValueError, SyntaxError, IndexError, ZeroDivisionError):
                                                    erragain()
                                            erragain()
                                    if verss.lower() == "n":
                                        esp()
                                    elif verss.lower() == "r":
                                        reselect()
                                    elif verss.lower() == "l":
                                        def select_list():
                                            cls()
                                            window_title(f'{SSTITLE} - Lista de versiones disponibles')
                                            day = getdate()
                                            print(f"{SSTITLE} - {day}\n--------------------------\n")
                                            print("VERSIONES ESTABLES:")
                                            for i, version in enumerate(MC_STABLE, start=1):
                                                print(f"(-) {version}")
                                            print('')
                                            print("VERSIONES SNAPSHOT:")
                                            for i, version in enumerate(MC_SNAPSHOT, start=1):
                                                print(f"(-) {version}")
                                            print('')
                                            print("VERSIONES DE APRIL'S FOOLS:")
                                            for i, version in enumerate(MC_APRILS, start=1):
                                                print(f"(-) {version}")
                                            print('')
                                            print("VERSIONES COMBAT TEST:")
                                            for i, version in enumerate(MC_COMBAT, start=1):
                                                print(f"(-) {version}")
                                            print('')
                                            print("VERSIONES ANTIGUAS:")
                                            for i, version in enumerate(MC_OLD, start=1):
                                                print(f"(-) {version}")
                                            listselection = input("\n(B) Atrás\n(R) Volver al menú principal\n\nEscribe una versión para instalar o elige una de las opciones=")
                                            try:
                                                if listselection.lower() == "b":
                                                    vers_select()
                                                elif listselection.lower() == "r":
                                                    esp()
                                                elif listselection.lower() in MC_STABLE.keys():
                                                    servdownload(listselection,"stable")
                                                elif listselection.lower() in MC_SNAPSHOT.keys():
                                                    servdownload(listselection,"snapshot")
                                                elif listselection.lower() in MC_APRILS.keys():
                                                    servdownload(listselection,"aprils")
                                                elif listselection.lower() in MC_COMBAT.keys():
                                                    servdownload(listselection,"combat")
                                                elif listselection.lower() in MC_OLD.keys():
                                                    servdownload(listselection,"old")
                                                else:
                                                    select_list()
                                            except (ValueError, SyntaxError, IndexError, ZeroDivisionError):
                                                select_list()
                                        select_list()
                                    elif verss.lower() in MC_STABLE.keys():
                                        servdownload(verss,"stable")
                                    elif verss.lower() in MC_SNAPSHOT.keys():
                                        servdownload(verss,"snapshot")
                                    elif verss.lower() in MC_APRILS.keys():
                                        servdownload(verss,"aprils")
                                    elif verss.lower() in MC_COMBAT.keys():
                                        servdownload(verss,"combat")
                                    elif verss.lower() in MC_OLD.keys():
                                        servdownload(verss,"old")
                                    else:
                                        vers_select()
                                except (ValueError, SyntaxError, IndexError, ZeroDivisionError):
                                    installmenu()
                            vers_select()
                        else:
                            installmenu()
                    reselect()
                elif inconf == 2:
                    esp()
                else:
                    installmenu()
            except (ValueError, SyntaxError, IndexError, ZeroDivisionError):
                installmenu()  

        # LICENSE AND EXTRAS
        def about():
            LOGGER.info("Entering Extras menu...")
            cls()
            window_title(f'{SSTITLE} - Acerca de {SSTITLE}')
            day = getdate()
            copyr = input(f"{SSTITLE} - {day}\n--------------------------\n\nMIT License - Copyright (c) {YEAR} ngdplnk\n\n{SSTITLE} {SSVERSION}\n\n{CHANGELOG_SPA}\n\n{HELPERS}\n\n-------------------------------------\n\n(1) Ver repositorio en el navegador\n(2) Ver licencia en el navegador\n(3) Volver al menú principal\n\nElige una de las opciones= ")
            try:
                if any(char in "0123456789+-*/" for char in copyr):
                    if not copyr[0].isalpha():
                        selec = eval(copyr)
                    else:
                        selec = copyr
                else:
                    selec = copyr
                selec = int(selec)
                if selec == 1:
                    url = colored("https://github.com/ngdplnk/SSTools4MC","cyan") # type: ignore
                    cls()
                    window_title(f'{SSTITLE} - Ver repositorio')
                    day = getdate()
                    input(f"{SSTITLE} - {day}\n--------------------------\n\nEl repositorio se abrirá en tu navegador.\n\n{url}\n\nPresiona ENTER para continuar.")
                    url = "https://github.com/ngdplnk/SSTools4MC"
                    webbrowser.open(url)
                    about()
                elif selec == 2:
                    url = colored("https://github.com/ngdplnk/SSTools4MC/blob/main/LICENSE","cyan") # type: ignore
                    cls()
                    window_title(f'{SSTITLE} - Ver licencia')
                    day = getdate()
                    input(f"{SSTITLE} - {day}\n--------------------------\n\nLa licencia se abrirá en tu navegador.\n\n{url}\n\nPresiona ENTER para continuar.")
                    url = "https://github.com/ngdplnk/SSTools4MC/blob/main/LICENSE"
                    webbrowser.open(url)
                    about()
                elif selec == 3:
                    esp()
                else:
                    about()
            except (ValueError, SyntaxError, IndexError, ZeroDivisionError):
                about()

        # EXIT
        def exiit():
            cls()
            window_title(f'{SSTITLE} - Nos vemos pronto!')
            print(f"--------------------------------------------\nNos vemos pronto!\nMIT License - Copyright (c) {YEAR} ngdplnk\n--------------------------------------------\n")
            time.sleep(1.2)
            LOGGER.info("QUITTING PROGRAM...")  
            sys.exit()

        # MAIN MENU
        def menu():
            LOGGER.info("Entering Main menu...")
            os.makedirs(SSTOOLS_FOLDER, exist_ok=True)
            os.chdir(SSTOOLS_FOLDER)
            cls()
            window_title(f'{SSTITLE} - Bienvenido! Estás en el menú principal')
            day = getdate()
            seleccion = input(f"{SSTITLE} - {day}\n--------------------------\n\nHola! Estás en el menú principal.\n\n(1) Inciar un Servidor\n(2) Instalar un Nuevo Servidor\n(3) Extras\n(4) Cambiar Lenguaje\n(5) Salir\n\nElige una de las opciones= ")
            try:
                if any(char in "0123456789+-*/" for char in seleccion):
                    if not seleccion[0].isalpha():
                        sel = eval(seleccion)
                    else:
                        sel = seleccion
                else:
                    sel = seleccion
                sel = int(sel)
                if sel == 1:
                    ram()
                elif sel == 2:
                    installmenu()
                elif sel == 3:
                    about()
                elif sel == 4:
                    eng()
                elif sel == 5:
                    exiit()
                menu()
            except (ValueError, SyntaxError, IndexError, ZeroDivisionError):
                menu()

        menu()

    # STARTUP
    def startup():
        # ICON
        LOGGER.info("Setting up icon...")
        ico = os.path.abspath(ICON_PATH)
        if not os.path.exists(ico):
            LOGGER.error("Icon not found")
        else:
            hIcon = ctypes.windll.user32.LoadImageW(
                None, ico, 1, 0, 0, 0x00000010
            )
            hwnd = ctypes.windll.kernel32.GetConsoleWindow()
            ctypes.windll.user32.SendMessageW(hwnd, 0x0080, 0, hIcon)
        # LANGUAGE
        if SYSTEM_LANG.startswith("es") or SYSTEM_LANG.startswith("Spanish"):
            esp()
        else:
            eng()

    # RUN PROGRAM
    startup()
except (Exception, KeyboardInterrupt) as e:
    LOGGER.critical(f"AN ERROR OCCURRED AND THE PROGRAM CLOSED UNEXPECTEDLY!!!")
    LOGGER.critical(f"The problem is described below:")
    if isinstance(e, KeyboardInterrupt):
        LOGGER.critical(f"KeyboardInterrupt triggered by User!!!")
    else:
        LOGGER.critical(f"{e}")

#### END OF PROGRAM ####