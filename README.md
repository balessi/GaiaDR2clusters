# File listing

File/Folder Name          | Description
------------------------- | -----------
/lists/GDR2_OK.txt        | Clusters with distances and/or kinematics derived by Gaia, Hipparcos or VLBI
/lists/GDR2_Trouble.txt   | Clusters with distances and or kinematics but with too many possible matches
/lists/GDR2_Rejected.txt  | Objects not included in the other lists for reasons explained in this file
/lists/GDR2_topcat.txt    | List for use with Topcat (import as an ASCII file)
/lists/ages.txt           | Ages and E(B-V) for clusters in the GDR2_OK list
/Python                   | Material used to derive parameters for clusters with ref 'Alessi (Gaia DR2)' in file GDR2_OK.txt

# What is the rationale of this work?

With so many open clusters discoveries in the last 2 years (thanks to Gaia) it is necessary to compile a merged catalog
identifying each cluster, discarding duplicates and distributing the names and aliases properly according to the discovery
precedence.
It is also necessary to join all that is new to the previous works (e.g. Dias, MWSC, etc) as well as my own and other
unpublished findings to arrive at a compreensible list of all things that are suitable for Gaia, while at the same time,
maintaining all obvious unphysical cases out.

# What are the sources I used to build this list?

1. My own personal list
1. Star clusters, associations, & candidates in the MW (Bica+, 2019)
1. Latest edition of the DAML catalog (and also wilton.unifei.edu.br)
1. MWSC catalog
1. Homogeneous Catalog of Open Cluster Param. (Loktin+, 2017)
1. Clusters discovered using Gaia DR1 or DR2 Data
   e.g. Gulliver, COIN-Gaia, UBC, UPK, Theia, FoF, etc (see reference for each cluster in the list's bibcode column)
1. Miscellaneous references
   e.g. Embedded clusters with VLBI parallaxes (e.g. 2014ApJ...783..130R)

# What criteria I used regarding the cluster names and aliases?

1. The main name is the name given by the discoverer who first noticed (and published) the cluster
1. The aliases are ordered more or less in the same fashion
1. Unpublished names (see Alessi and DSH below) where used only for unique objects not yet published
   by any professional researcher, otherwise they are depicted as aliases and usually in the first position

## Name precedence

Gaia 1-7 > OPD > Loktin-Popova > [APOGEE 6D] > Gulliver > UBC 1-32 > BBJ > NEST > Bica > Vela Ring >
UFMG > COIN-Gaia > UBC 33-90 > Theia > HMAC > Gaia 8 > Clusterix > UPK > BBJ nx > FoF > UBC 91-672 >
OC-n > Theia 1641-

Designation  | Sequence  | Published
------------ | --------- | ---------------
Gaia         | 1-2       | Feb 2017 (arXiv)
OPD          | all       | Jun 2017
Loktin-Popova| all       | Jul 2017
Gaia         | 3-7       | May 2018 (arXiv)
<APOGEE 6D>  | all       | Sep 2018
Gulliver     | all       | Oct 2018
UBC          | 1-32      | Oct 2018
BBJ          | 1-6       | Nov 2018
NEST         | all       | Nov 2018
Bica         | all       | Jan 2019
Vel Ring     | all       | Jan 2019
UFMG         | all       | Mar 2019
COIN-Gaia    | all       | Apr 2019
UBC          | 33-90     | Jul 2019
Theia        | 1-1640    | Sep 2019
HMAC         | all       | Sep 2019
Gaia         | 8         | Sep 2019 (arXiv)
Clusterix    | all       | Oct 2019 (arXiv)
UPK          | all       | Oct 2019
BBJ          | 1b,2b,3b  | Nov 2019 (arXiv)
FoF          | all       | Dec 2019
UBC          | 91-672    | Mar 2020
OC           | all       | Mar 2020
Theia        | 1641-8313 | Apr 2020 (arXiv)

# What is the meaning and origin of some unknow names in the list?

## I - Recent unpublished (re)discoveries by Bruno Alessi after 2017

Full Name               |  Acronym   |   Meaning
----------------------- | ---------- | ---------------
2MASS Jhhmm-ddmm        |            | Cluster candidates found while examining 2MASS images with Aladin
Akari-WISE-Gaia         |   AWG      | Cluster candidates found examining images from Akari and WISE surveys and checked with Gaia DR2
Aladin                  |            | Cluster candidates found (mainly in Crux and Scutum) while examining DSS2 images with Aladin
Cartes du Ciel          |   CdC      | Cluster candidates found when searching for groups of Tycho-2 stars with similar motions using the software Cartes du Ciel
Cha I SW                |            | Cluster candidate found while examining the region around Cha I
Eta PsA Cl              |            | Cluster or Moving Group candidate found while examining Tycho-2 stars using Cartes du Ciel
GN 14.26.8 Cl           |            | Embedded cluster candidate found wile checking for clusters associated to bright nebulae in Aladin
Gaia-TGAS               |            | Cluster candidate found while examining DSS2 images with Aladin and checking with Gaia-TGas
Latyshev 2              |            | Very nearby, unstudied, cluster or MG candidate already listed in Lund Catalog. Seems to be real.
PanSTARRS Jhhmm-ddmm    |   PS       | Cluster candidates found while examining PanSTARRS images with Aladin
Spitzer Jhhmm-ddmm      |            | Cluster candidates found while examining Spitzer images with Aladin
Urquhart Gddd.mm+/-dd.mm|   Urq      | Embedded cluster candidates found while checking Spitzer or 2MASS images with Aladin for sources listed in 2014MNRAS.443.1555U
VVV Jhhmm-ddmm          |            | Cluster candidates found while examining VVV images with Aladin
WISE Jhhmm-ddmm         |            | Cluster candidates found while examining WISE images with Aladin, but not checked with Gaia
WISE-Gaia               |   WG       | Cluster candidates found while examining WISE images with Aladin and checked with Gaia DR2
Zeta CrB Cl             |            | Cluster or Moving Group candidate found while checking if Higher order multiple stars have or have not more companions forming a small Cl

## II - Asterisms and cluster candidates found by the DSH (Deep-Sky Hunters) fellows.
Few of them are published (e.g. Alessi, Kronberger, Teutsch), but the majority is still unpublished

<Bayer desig> Grp, Alessi, Alessi-Teutsch, Caucal, DSH Jhhmm+/-ddmm, Desvoivres, Eklund, El Kanbi,
El Kanbi-Prestgard, Ferrero, HD nnnnnn Grp, Juchert, Juchert-Saloranta, Karhula, Kernya, Kernya-Santa,
Kn-DeCAPS, Kronberger, Kronberger-Patchick, Kupco, Pa-DeCAPS, Patchick, Ponsot, Pothier, Prestgard,
Raymond, Renou, Riddle, Saloranta, Salque, Santa, Schoenball, Slotegraaf, Steine, Streicher, Strottner,
TC hhmm+/-ddmm, TYC nnnn-nnnn Grp, Teutsch, Toepler, Vastagh, Wallace, Zannin, van Wulfen

## III - Few new not well known clusters found in the literature

Designation                              |  Reference
---------------------------------------- | ------------
<star_name> Subgr, e.g. "HR 8352 Subgr"  | subgroups discovered by Eric Mamajek in the GAYA young association
AWJ ddd.mm-dd.mm                         | arXiv:1807.09262v1
BBJ nx (e.g. BBJ 1b)                     | arXiv:1911.05709v1
Iss                                      | The infamous Isserstedt rings
Lin-Chen                                 | Unpublished catalog, mentioned in three articles: arXiv:1111.7179v2, 2015IAUGA..2254260L, 2017IAUS..316..163L
Loktin-Popova                            | Homogeneous Catalog of Open Cluster Param. (Loktin+, 2017)
Me'lnik-Efremov                          | New list of OB associations (Me'lnik+, 1995)
OC-nn (e.g. OC-1)                        | 2020PASP..132c4502H
OSC ddd.mm-dd.mm                         | A Search for New Open Clusters Hosting Cepheids (Glushkova et al.)
Russeil                                  | Star-forming complexes and the spiral structure of our Galaxy (Russeil)

## IV - 'FoF' acronym adoption and cluster selection

Althoug Cantat-Gaudin et al. used 'LP' (Liu-Pang) for the objects listed in arXiv:1910.12600v1, I opted to use
'FoF' because the authors used this acronym to name their dicoveries in a sample table in their article.
'FoF' stands for 'Friends-of-Friends', which is the name of the algorithm they used to find the clusters

I tried to use as most as I can of their huge list of more than 2K clusters.

My criteria for exclusion was:
1. The cluster is dubious (class 3), and
2. The cluster has many cross-matched IDs in the same catalog turning their
   correct identification difficult (which set of parameters should I use?)

# What criteria I used to design a type to each object and whar are their meanings?

I checked the physical radiuses of all previously known objects listed as 'OC' (Open Cluster) and found thay they rarely
are larger than 10 Pc, while Associations and Moving Groups extends to tens (sometimes hundreds) of parsecs.

I did not used this 10 pc criteria to classify FoF clusters because their listed radius included the most remote
member, so I thought their main concentrations would be considerably smaller that what their radiuses indicates...
but after seeing their charts, I noticed that that is not true for many of them who looks like streams or associations
with no defined concentration.

1. 'Asc' = Unclassified association of some sort (could be 'YAs', 'MG', etc, it's physical diam is larger than 10 Pc)
1. 'EC'  = Embedded Open Cluster or group
1. 'GC'  = Globular Cluster
1. 'MG'  = Moving Group (old, mostly low-mass stars and log_t > ~8.3)
1. 'NC'  = Nuclear Cluster
1. 'OB'  = OB association (massive OB stars and log_t always considerably lower than 8)
1. 'OC'  = 'Ordinary' Open Cluster (the physical diameter is less than 10 pc, with few exceptions)
1. 'RSG' = Cluster of Red Supergiants
1. 'SFR' = Star-Forming Region (probably OB assoc or young cluster plus nebulosity)
1. 'SSC' = Super star cluster (mass > 10^4 Suns)
1. 'Str' = String (as defined by Marina Kounkel in her article)
1. 'UFD' = Ultra-Faint Dwarf, which are objects with characterists of 
1. 'YAs' = Young Association (low-mass stars and log_t < ~8.3)
 
# What criteria and procedure I used in my matching process?

1. The center-to-center separation is less than the sum of the radius of the two clusters involved.
1. One cluster in a matched pair must not have a radius more than 10 times larger than the other
   otherwise, we could eliminate distinct subclusters or clusters embedded in a larger structure.
1. The parallaxes, proper motions and radial velocities (if available) must be equal given it's errors
   when one value (e.g. RV) is not available for one cluster in the pair it is not used in the comparison.
1. When the values are available but the associated errors are not, I used debault values (e.g. 0.3 mas for parallaxes)
1. The matches are doing only between clusters with distinct references. Here I take for granted that the reference
    don't list duplicates (Exception: FoF - see comment in the section 'IV FoF acronym adoption and cluster selection' above).
1. Sometimes I multiplied the errors by a factor between 1.0 or 2.5 because some clearly matches were not detected.
   The reason is that the references listed rather dissimilar values, e.g., for motions and distance. This is more common
   when matching a cluster with Gaia DR2 data to another with pre-Gaia data.
1. The cluster types and ages were not considered in the matching process. For example, many FoF clusters matched to known Globulars.
   If I treated them all as OCs and used type to disciminate they would not be matched.
1. After generating all possible matches for a given cluster, I did a careful visual check to choose the most probable match.
1. When the object has too many possible matches, I relegated it to the list named 'GDR2_Trouble.txt'.
   When I am unsure if the match is correct, I put a '?' just before the alias name.
1. Since they are usually very large and irregular, I also examined charts of Theia and OPD groups to see if the match is possible
   or not - for instance, some UPK detections seems to be the main concentration in their corresponding Theia groups.
1. When necessary, I used Topcat and Aladin to refine the matches.
1. For some pre-Gaia discoveries (e.g. Escorial, Platais, Melnik's OB associations), I downloaded the list of members and cross-matched
   them with Gaia DR2 to derive average distances and motions prior to matching them.

# What means those weird 'Alessi' references in the list?

The distances and proper motions for clusters listed under the following references are my own estimates:

1. 'Alessi (Gaia DR2)'   possible clusters with Gaia DR2 distances and motions estimates
1. 'Alessi (Gaia-TGAS)'  possible clusters with Gaia-TGAS distances and motions estimates

I do not expect that all of them are true positives, but I hope a sizeable number of them are genuine physical systems
I included them because my aim was to build a most compreensible possible list of clusters suitable for Gaia, thus I think
that while all obvious unphysical cases were left out, many potential candidates are in this list.

# What is not included in this list?

1. Obvious asterisms.
1. Faint and/or very compact, mostly embedded clusters not accessible with Gaia.
1. Very large Moving Groups or Associations without a defined center because they cover most of the sky if not the entire sky.
   I arbitrarily excluded objects with a diameter larger than 1 Radian - ~57.3 degrees or 3438 arcminutes.
1. Moving Groups and streams in the MW Halo.
1. Objects which I was unable to find using Aladin in any Wavelenght (e.g. some IR clusters claimed by Bica, Camargo, etc).
   Either they are really very faint, are asterisms/artifacts or have coordinates/diameters in error.

# What still needs to be done?

1. The diameters are far from homogeneous - sometimes they include only the stars in the cluster's center or main concentrations
   sometimes they includes stars far in the cluster's halo or even in associated tails and streams (e.g. many Theias).
1. I'm aware that there are still coordinates in error. But they are few and not too far off.
   Besides, all coordinates should follow a rule, e.g. marks the point of highest density. Then, like diameters, coordinates are
   also far from being homogeneous.
1. I think I could have missed some RV values in the process of merging all those sources!
1. Some clusters or associations (e.g. NGC 1893, 2264, ...) includes many smaller clusters or subclusters, but the listed motions and distances
   refer only to them as a whole or to few of them. In that cases, should I list all, some (those who has pars and/or pms) or only one?
1. Includes the associated measurement errors.
1. Use machine-friendly values for radius (degrees) and parallax instead of distances in parsecs.
1. Adjust the measurements significant digits after considering their associated errors.
1. HUGE! match and includes the objects and data in the forthcoming works of the Barcelona Group and Marina Kounkel et al.
