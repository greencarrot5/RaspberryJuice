class Entity:
    '''Minecraft PI entity description. Can be sent to Minecraft.spawnEntity'''

    def __init__(self, id, name = None):
        self.id = id
        self.name = name

    def __cmp__(self, rhs):
        return hash(self) - hash(rhs)

    def __eq__(self, rhs):
        return self.id == rhs.id

    def __hash__(self):
        return self.id

    def __iter__(self):
        '''Allows an Entity to be sent whenever id is needed'''
        return iter((self.id,))

    def __repr__(self):
        return 'Entity(%d)'%(self.id)

EXPERIENCE_ORB=Entity(2)
AREA_EFFECT_CLOUD=Entity(3)
ELDER_GUARDIAN=Entity(4)
WITHER_SKELETON=Entity(5)
STRAY=Entity(6)
EGG=Entity(7)
LEASH_HITCH=Entity(8)
PAINTING=Entity(9)
ARROW=Entity(10)
SNOWBALL=Entity(11)
FIREBALL=Entity(12)
SMALL_FIREBALL=Entity(13)
ENDER_PEARL=Entity(14)
ENDER_SIGNAL=Entity(15)
THROWN_EXP_BOTTLE=Entity(17)
ITEM_FRAME=Entity(18)
WITHER_SKULL=Entity(19)
PRIMED_TNT=Entity(20)
HUSK=Entity(23)
SPECTRAL_ARROW=Entity(24)
SHULKER_BULLET=Entity(25)
DRAGON_FIREBALL=Entity(26)
ZOMBIE_VILLAGER=Entity(27)
SKELETON_HORSE=Entity(28)
ZOMBIE_HORSE=Entity(29)
ARMOR_STAND=Entity(30)
DONKEY=Entity(31)
MULE=Entity(32)
EVOKER_FANGS=Entity(33)
EVOKER=Entity(34)
VEX=Entity(35)
VINDICATOR=Entity(36)
ILLUSIONER=Entity(37)
MINECART_COMMAND=Entity(40)
BOAT=Entity(41)
MINECART=Entity(42)
MINECART_CHEST=Entity(43)
MINECART_FURNACE=Entity(44)
MINECART_TNT=Entity(45)
MINECART_HOPPER=Entity(46)
MINECART_MOB_SPAWNER=Entity(47)
CREEPER=Entity(50)
SKELETON=Entity(51)
SPIDER=Entity(52)
GIANT=Entity(53)
ZOMBIE=Entity(54)
SLIME=Entity(55)
GHAST=Entity(56)
PIG_ZOMBIE=Entity(57)
ENDERMAN=Entity(58)
CAVE_SPIDER=Entity(59)
SILVERFISH=Entity(60)
BLAZE=Entity(61)
MAGMA_CUBE=Entity(62)
ENDER_DRAGON=Entity(63)
WITHER=Entity(64)
BAT=Entity(65)
WITCH=Entity(66)
ENDERMITE=Entity(67)
GUARDIAN=Entity(68)
SHULKER=Entity(69)
PIG=Entity(90)
SHEEP=Entity(91)
COW=Entity(92)
CHICKEN=Entity(93)
SQUID=Entity(94)
WOLF=Entity(95)
MUSHROOM_COW=Entity(96)
SNOWMAN=Entity(97)
OCELOT=Entity(98)
IRON_GOLEM=Entity(99)
HORSE=Entity(100)
RABBIT=Entity(101)
POLAR_BEAR=Entity(102)
LLAMA=Entity(103)
LLAMA_SPIT=Entity(104)
PARROT=Entity(105)
VILLAGER=Entity(120)
ENDER_CRYSTAL=Entity(200)
