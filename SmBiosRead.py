import os, sys
import ctypes
import ctypes.wintypes

# typedef struct _RawSMBIOSData
# {
#     BYTE    Used20CallingMethod;
#     BYTE    SMBIOSMajorVersion;
#     BYTE    SMBIOSMinorVersion;
#     BYTE    DmiRevision;
#     DWORD   Length;
#     BYTE    SMBIOSTableData[];
# } RawSMBIOSData;

class RawSMBIOSData(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ('Used20CallingMethod', ctypes.c_byte),
        ('SMBIOSMajorVersion', ctypes.c_byte),
        ('SMBIOSMinorVersion', ctypes.c_byte),
        ('DmiRevision', ctypes.c_byte),
        ('Length', ctypes.c_ulong),
        ('SMBIOSTableData', ctypes.c_char_p),
    ]

# ///
# /// The Smbios structure header.
# ///
# typedef struct {
#   UINT8          Type;
#   UINT8          Length;
#   UINT16         Handle;
# } SMBIOS_STRUCTURE;

class SMBIOS_STRUCTURE(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ('Type', ctypes.c_uint8),
        ('Length', ctypes.c_uint8),
        ('Handle', ctypes.c_uint16),
    ]

# ///
# /// BIOS Characteristics
# /// Defines which functions the BIOS supports. PCI, PCMCIA, Flash, etc.
# ///
# typedef struct {
#   UINT32  Reserved                          :2;  ///< Bits 0-1.
#   UINT32  Unknown                           :1;
#   UINT32  BiosCharacteristicsNotSupported   :1;
#   UINT32  IsaIsSupported                    :1;
#   UINT32  McaIsSupported                    :1;
#   UINT32  EisaIsSupported                   :1;
#   UINT32  PciIsSupported                    :1;
#   UINT32  PcmciaIsSupported                 :1;
#   UINT32  PlugAndPlayIsSupported            :1;
#   UINT32  ApmIsSupported                    :1;
#   UINT32  BiosIsUpgradable                  :1;
#   UINT32  BiosShadowingAllowed              :1;
#   UINT32  VlVesaIsSupported                 :1;
#   UINT32  EscdSupportIsAvailable            :1;
#   UINT32  BootFromCdIsSupported             :1;
#   UINT32  SelectableBootIsSupported         :1;
#   UINT32  RomBiosIsSocketed                 :1;
#   UINT32  BootFromPcmciaIsSupported         :1;
#   UINT32  EDDSpecificationIsSupported       :1;
#   UINT32  JapaneseNecFloppyIsSupported      :1;
#   UINT32  JapaneseToshibaFloppyIsSupported  :1;
#   UINT32  Floppy525_360IsSupported          :1;
#   UINT32  Floppy525_12IsSupported           :1;
#   UINT32  Floppy35_720IsSupported           :1;
#   UINT32  Floppy35_288IsSupported           :1;
#   UINT32  PrintScreenIsSupported            :1;
#   UINT32  Keyboard8042IsSupported           :1;
#   UINT32  SerialIsSupported                 :1;
#   UINT32  PrinterIsSupported                :1;
#   UINT32  CgaMonoIsSupported                :1;
#   UINT32  NecPc98                           :1;
#   UINT32  ReservedForVendor                 :32; ///< Bits 32-63. Bits 32-47 reserved for BIOS vendor
#                                                  ///< and bits 48-63 reserved for System Vendor.
# } MISC_BIOS_CHARACTERISTICS;

class MISC_BIOS_CHARACTERISTICS(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ('Reserved', ctypes.c_uint32, 2),
        ('Unknown', ctypes.c_uint32, 1),
        ('BiosCharacteristicsNotSupported', ctypes.c_uint32, 1),
        ('IsaIsSupported', ctypes.c_uint32, 1),
        ('McaIsSupported', ctypes.c_uint32, 1),
        ('EisaIsSupported', ctypes.c_uint32, 1),
        ('PciIsSupported', ctypes.c_uint32, 1),
        ('PcmciaIsSupported', ctypes.c_uint32, 1),
        ('PlugAndPlayIsSupported', ctypes.c_uint32, 1),
        ('ApmIsSupported', ctypes.c_uint32, 1),
        ('BiosIsUpgradable', ctypes.c_uint32, 1),
        ('BiosShadowingAllowed', ctypes.c_uint32, 1),
        ('VlVesaIsSupported', ctypes.c_uint32, 1),
        ('EscdSupportIsAvailable', ctypes.c_uint32, 1),
        ('BootFromCdIsSupported', ctypes.c_uint32, 1),
        ('SelectableBootIsSupported', ctypes.c_uint32, 1),
        ('RomBiosIsSocketed', ctypes.c_uint32, 1),
        ('BootFromPcmciaIsSupported', ctypes.c_uint32, 1),
        ('EDDSpecificationIsSupported', ctypes.c_uint32, 1),
        ('JapaneseNecFloppyIsSupported', ctypes.c_uint32, 1),
        ('JapaneseToshibaFloppyIsSupported', ctypes.c_uint32, 1),
        ('Floppy525_360IsSupported', ctypes.c_uint32, 1),
        ('Floppy525_12IsSupported', ctypes.c_uint32, 1),
        ('Floppy35_720IsSupported', ctypes.c_uint32, 1),
        ('Floppy35_288IsSupported', ctypes.c_uint32, 1),
        ('PrintScreenIsSupported', ctypes.c_uint32, 1),
        ('Keyboard8042IsSupported', ctypes.c_uint32, 1),
        ('SerialIsSupported', ctypes.c_uint32, 1),
        ('PrinterIsSupported', ctypes.c_uint32, 1),
        ('CgaMonoIsSupported', ctypes.c_uint32, 1),
        ('NecPc98', ctypes.c_uint32, 1),
        ('ReservedForVendor', ctypes.c_uint32),
    ]

# ///
# /// Extended BIOS ROM size.
# ///
# typedef struct {
#   UINT16 Size           :14;
#   UINT16 Unit           :2;
# } EXTENDED_BIOS_ROM_SIZE;

class EXTENDED_BIOS_ROM_SIZE(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ('Size', ctypes.c_uint16, 14),
        ('Unit', ctypes.c_uint16, 2),
    ]

# typedef UINT8 SMBIOS_TABLE_STRING;
# typedef struct {
#   SMBIOS_STRUCTURE          Hdr;
#   SMBIOS_TABLE_STRING       Vendor;
#   SMBIOS_TABLE_STRING       BiosVersion;
#   UINT16                    BiosSegment;
#   SMBIOS_TABLE_STRING       BiosReleaseDate;
#   UINT8                     BiosSize;
#   MISC_BIOS_CHARACTERISTICS BiosCharacteristics;
#   UINT8                     BIOSCharacteristicsExtensionBytes[2];
#   UINT8                     SystemBiosMajorRelease;
#   UINT8                     SystemBiosMinorRelease;
#   UINT8                     EmbeddedControllerFirmwareMajorRelease;
#   UINT8                     EmbeddedControllerFirmwareMinorRelease;
#   //
#   // Add for smbios 3.1.0
#   //
#   EXTENDED_BIOS_ROM_SIZE    ExtendedBiosSize;
# } SMBIOS_TABLE_TYPE0;

class SMBIOS_TABLE_TYPE0(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ('Hdr',                                    SMBIOS_STRUCTURE),
        ('Vendor',                                 ctypes.c_uint8),
        ('BiosVersion',                            ctypes.c_uint8),
        ('BiosSegment',                            ctypes.c_uint16),
        ('BiosReleaseDate',                        ctypes.c_uint8),
        ('BiosSize',                               ctypes.c_uint8),
        ('BiosCharacteristics',                    MISC_BIOS_CHARACTERISTICS),
        ('BIOSCharacteristicsExtensionBytes',      ctypes.c_uint8 * 2),
        ('SystemBiosMajorRelease',                 ctypes.c_uint8),
        ('SystemBiosMinorRelease',                 ctypes.c_uint8),
        ('EmbeddedControllerFirmwareMajorRelease', ctypes.c_uint8),
        ('EmbeddedControllerFirmwareMinorRelease', ctypes.c_uint8),
        ('ExtendedBiosSize',                       ctypes.c_uint8),
    ]

def GetSmBiosTypeStr(Buffer, Index):
    EndIndex = 0
    while (Buffer[EndIndex] !=0) or (Buffer[EndIndex + 1] != 0):
        EndIndex += 1
    EndIndex += 2

    StrIndex = 1
    StrStartIndex = 0
    StrEndIndex   = 0
    while True:
        while Buffer[StrEndIndex] != 0:
            StrEndIndex += 1
        StrEndIndex += 1
        if StrEndIndex >= EndIndex:
            break
        if Index == StrIndex:
            return Buffer[StrStartIndex: StrEndIndex].decode('utf-8')
        StrStartIndex = StrEndIndex
        StrIndex += 1

def DisPatchStructType(Buffer):
    Header = SMBIOS_STRUCTURE.from_buffer_copy(Buffer)

    if Header.Type == 0:
        SmBiosType0 = SMBIOS_TABLE_TYPE0.from_buffer_copy(Buffer)
        print('Type0 : Vendor : {0}'.format(GetSmBiosTypeStr(Buffer[Header.Length:], SmBiosType0.Vendor)))
        print('Type0 : BiosVersion : {0}'.format(GetSmBiosTypeStr(Buffer[Header.Length:], SmBiosType0.BiosVersion)))
        print('Type0 : BiosReleaseDate : {0}'.format(GetSmBiosTypeStr(Buffer[Header.Length:], SmBiosType0.BiosReleaseDate)))

def ParsingSmBiosData(Buffer, Length):
    StartIndex = 0
    MaxIndex   = Length - 1

    while True:
        # Check Header Type
        Header = SMBIOS_STRUCTURE.from_buffer_copy(Buffer[StartIndex:])
        # DisPatch SmBios TypeX's String Area
        DisPatchStructType(Buffer[StartIndex:])

        if (Header.Type == 127) and (Header.Length == 4):
            break

        # Get the SmBios Typex's whole range
        EndIndex = StartIndex + Header.Length
        while (Buffer[EndIndex] != 0) or (Buffer[EndIndex + 1] != 0):
            EndIndex += 1
        EndIndex += 2

        if EndIndex >= MaxIndex:
            break

        StartIndex = EndIndex

def GetSmbiosInfo():
    Kernel32 = ctypes.windll.kernel32

    if Kernel32 == None:
        raise Exception('Could not load Kernel32')

    Signature_RSMB = ctypes.wintypes.DWORD(int.from_bytes(b'RSMB', 'big'))
    RSMB_TableID   = ctypes.wintypes.DWORD(0)
    Buffer         = ctypes.create_string_buffer(0)
    BufferSize     = ctypes.wintypes.DWORD(0)

    ReturnSize = Kernel32.GetSystemFirmwareTable(Signature_RSMB, RSMB_TableID, Buffer, BufferSize)
    if ReturnSize == 0:
        raise Exception('Could not get RSMB table')

    BufferSize.value = ReturnSize
    Buffer = ctypes.create_string_buffer(BufferSize.value)

    ReturnCode = Kernel32.GetSystemFirmwareTable(Signature_RSMB, RSMB_TableID, Buffer, BufferSize)
    if ReturnSize != ReturnCode:
        raise Exception('Could not get total RSMB table')

    SmBiosData = RawSMBIOSData.from_buffer_copy(Buffer.raw)
    SmBiosData_Length = SmBiosData.Length
    SmBiosData_Buffer = Buffer.raw[RawSMBIOSData.SMBIOSTableData.offset:]
    ParsingSmBiosData(SmBiosData_Buffer, SmBiosData_Length)

def main():
    Status = 0

    GetSmbiosInfo()

    return Status

if __name__ == "__main__":
    sys.exit(main())