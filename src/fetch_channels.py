# fetch_channels.py

# List of YouTube channel IDs and names
CHANNELS = [
    {'channel_id': 'UC_x5XG1OV2P6uZZ5b3t5t6Q', 'channel_name': 'Google Developers'},
    {'channel_id': 'UCk9p0p_zLlP9tQnxHxsXjQ', 'channel_name': 'Google Cloud'},
    {'channel_id': 'UCaKZDEMDdQc8t6GzFj1_TDw', 'channel_name': 'Be Inspired'},
    {'channel_id': 'UCKZozRVHRYsYHGEyNKuhhdA', 'channel_name': 'Think School'},
    {'channel_id': 'UCsQoiOrh7jzKmE8NBofhTnQ', 'channel_name': 'Varun Mayya'},
    {'channel_id': 'UC-CSyyi47VX1lD9zyeABW3w', 'channel_name': 'Dhruv Rathee'},
    {'channel_id': 'UC5fcjujOsqD-126Chn_BAuA', 'channel_name': 'Sarthak Goswami'},
    {'channel_id': 'UC6WzPg6yxF9dQx2_O6R4lww', 'channel_name': 'Nitesh Rajput'},
    {'channel_id': 'UCz4a7agVFr1TxU-mpAP8hkw', 'channel_name': 'Mohak Mangal'},
    {'channel_id': 'UCKop7_gs7xq5tbrDDYuplhA', 'channel_name': 'RJRaunac'},
    {'channel_id': 'UCRgMIwmmh1-2k5HeTQ2cdkQ', 'channel_name': 'Gaurav Thakur'},
    {'channel_id': 'UC5n-0ihUiOuuvZSSUnMNZLw', 'channel_name': 'nikitaksthakur'},
    {'channel_id': 'UC7eZNThpjgXe5H0QwBN-XsQ', 'channel_name': 'mensxp'},
    {'channel_id': 'UCPJ_UzD4PEC-_vwN32amlIQ', 'channel_name': 'openletteryt'},
    {'channel_id': 'UCLXo7UDZvByw2ixzpQCufnA', 'channel_name': 'Vox'},
    {'channel_id': 'UCoOae5nYA7VqaXzerajD0lg', 'channel_name': 'Ali Abdaal'},
    {'channel_id': 'UCmGSJVG3mCRXVOP4yZrU1Dw', 'channel_name': 'johnnyharris'},
    {'channel_id': 'UCHnyfMqiRRG1u-2MsSQLbXA', 'channel_name': 'veritasium'},
    {'channel_id': 'UCK-HHyVCfKYzhxVOJgBt73w', 'channel_name': 'Keerthi History'},
    {'channel_id': 'UCsDTy8jvHcwMvSZf_JGi-FA', 'channel_name': 'Abhi and Niyu'},
    {'channel_id': 'UCs0kMbzhUYV2lhIV7xoWhoA', 'channel_name': 'The Sham Sharma Show'},
    {'channel_id': 'UC53cAvFeWsNwsfCQnJmLjDQ', 'channel_name': 'Satvic Movement'},
    {'channel_id': 'UC3w193M5tYPJqF0Hi-7U-2g', 'channel_name': 'Dr. Eric Berg DC'},
    {'channel_id': 'UCR9ygnRBOt8qfSbkCwOA3pw', 'channel_name': 'Samurai Matcha'},
    {'channel_id': 'UCnRVL1-HJnXWB_Xi2dAoTcg', 'channel_name': 'Bryan Johnson'},
    {'channel_id': 'UC2D2CMWXMOVWx7giW1n3LIg', 'channel_name': 'Andrew Huberman'},
    {'channel_id': 'UCa09am-cOsC-FSgr_nLkFFA', 'channel_name': 'ZOE'},
    {'channel_id': 'UCP4k407eomZThGHo_9sgMkg', 'channel_name': 'Dr. Pal'},
    {'channel_id': 'UCXmAKxh_qFL5703W9VPgpnA', 'channel_name': 'Foodpharmer'},
    {'channel_id': 'UCswH8ovgUp5Bdg-0_JTYFNw', 'channel_name': 'Russell Brand'},
    {'channel_id': 'UCnQC_G5Xsjhp9fEJKuIcrSw', 'channel_name': 'Ben Shapiro'},
    {'channel_id': 'UCNAxrHudMfdzNi6NxruKPLw', 'channel_name': 'Sam Harris'},
    {'channel_id': 'UCzQUP1qoWDoEbmsQxvdjxgQ', 'channel_name': 'PowerfulJRE'},
    {'channel_id': 'UCLwNTXWEjVd2qIHLcXxQWxA', 'channel_name': 'Timcast IRL'},
    {'channel_id': 'UCIHdDJ0tjn_3j-FS7s_X1kQ', 'channel_name': 'Valuetainment'},
    {'channel_id': 'UCGeBogGDZ9W3dsGx-mWQGJA', 'channel_name': 'IMPAULSIVE'},
    {'channel_id': 'UCpjlh0e319ksmoOD7bQFSiw', 'channel_name': 'Rich Roll'},
    {'channel_id': 'UCSHZKyawb77ixDdsGog4iWA', 'channel_name': 'lexfridman'},
    {'channel_id': 'UCGttrUON87gWfU6dMWm1fcA', 'channel_name': 'TuckerCarlson'},
    {'channel_id': 'UCNNTZgxNQuBrhbO0VrG8woA', 'channel_name': 'NoJumper'},
    {'channel_id': 'UCKsP3v2JeT2hWI_HzkxWiMA', 'channel_name': 'lewishowes'},
    {'channel_id': 'UC604SM0YhltEKZ5hmDs_Gqw', 'channel_name': 'AubreyMarcusPod'},
    {'channel_id': 'UC5AQEUAwCh1sGDvkQtkDWUQ', 'channel_name': 'TheoVon'},
    {'channel_id': 'UC5PstSsGrRwj2o6asQpC4Rg', 'channel_name': 'OfficialFlagrant'},
    {'channel_id': 'UChPuCAEXg7iYkVNjQY1NGYg', 'channel_name': 'FULLSENDPODCAST'},
    {'channel_id': 'UCIaH-gZIVC432YRjNVvnyCA', 'channel_name': 'ChrisWillx'},
    {'channel_id': 'UCGq-a57w-aPwyi3pW7XLiHw', 'channel_name': 'The Diary Of A CEO'},
    {'channel_id': 'UCkoujZQZatbqy4KGcgjpVxQ', 'channel_name': 'ShawnRyanShow'},
    {'channel_id': 'UCL_f53ZEJxp8TtlOkHwMV9Q', 'channel_name': 'Jordan B Peterson'},
    {'channel_id': 'UC0rE2qq81of4fojo-KhO5rg', 'channel_name': 'tanmaybhat'},
    {'channel_id': 'UCqJ4x3oLggFz5s6Djg5y7EQ', 'channel_name': 'UnfilteredThugesh'},
    {'channel_id': 'UCjdjyjdcdmldCK5XuuWbn1A', 'channel_name': 'AndreoBee'},
    {'channel_id': 'UCi5kSELjaJWmnBKPXkTcxsA', 'channel_name': 'fukrainsaanlive4744'},
    {'channel_id': 'UCejXQsQ7DZxlG15mlgVT5zA', 'channel_name': 'D-monchik'},
    {'channel_id': 'UCAov2BBv1ZJav0c_yHEciAw', 'channel_name': 'Samay Raina'},
    {'channel_id': 'UC7IcJI8PUf5Z3zKxnZvTBog', 'channel_name': 'The School of Life'},
    {'channel_id': 'UCl8TEoIOnMq_5ntJOYMq-Zg', 'channel_name': 'Dr Julie'},
    {'channel_id': 'UCL2QpphEeZFYwk6-WXD6hpA', 'channel_name': 'Dr. Tracey Marks'},
    {'channel_id': 'UClHVl2N3jPEbkNJVx-ItQIQ', 'channel_name': 'HealthyGamerGG'},
    {'channel_id': 'UCzBYOHyEEzlkRdDOSobbpvw', 'channel_name': 'Kati Morton'},
    {'channel_id': 'UCyGOloOIJWt8NlE4tnejQeA', 'channel_name': 'MedCircle'},
    {'channel_id': 'UCkJEpR7JmS36tajD34Gp4VA', 'channel_name': 'Psych2Go'},
    {'channel_id': 'UCpuqYFKLkcEryEieomiAv3Q', 'channel_name': 'Therapy in a Nutshell'},
    {'channel_id': 'UCR_Tzu1r5M9uoNB3CF4Zg3g', 'channel_name': 'Sidwarrier'},
    {'channel_id': 'UC-nPM1_kSZf91ZGkcgy_95Q', 'channel_name': 'HowtoADHD'},
    {'channel_id': 'UCCYX4s1DCn51Hpf1peHS30Q', 'channel_name': 'CinemaTherapyShow'},
    {'channel_id': 'UCmTM_hPCeckqN3cPWtYZZcg', 'channel_name': 'The Deshbhakt'},
    {'channel_id': 'UCwSPxg9bl8zAFBr5KlUiaWw', 'channel_name': 'sinhasushant'},
    {'channel_id': 'UCwWhs_6x42TyRM4Wstoq8HA', 'channel_name': 'The Daily Show'},
    {'channel_id': 'UCz8QaiQxApLq8sLNcszYyJw', 'channel_name': 'Firstpost'},
    {'channel_id': 'UC0yXUUIaPVAqZLgRjvtMftw', 'channel_name': 'Ravish Kumar Official'},
    {'channel_id': 'UCkquFW943phrj5RbNqtqj4w', 'channel_name': 'Ajit Anjum'},
    {'channel_id': 'UCfA29qhHnOQrEr7yjHsP9Jw', 'channel_name': 'Abhisar Sharma'},
    {'channel_id': 'UCx8Z14PpntdaxCt2hakbQLQ', 'channel_name': 'The Lallantop'},
    {'channel_id': 'UCuyRsHZILrU7ZDIAbGASHdA', 'channel_name': 'ThePrint'},
    {'channel_id': 'UCrC8mOqJQpoB7NuIMKIS6rQ', 'channel_name': 'StudyIQ IAS'},
    {'channel_id': 'UCkuZJIhMYCnOa0dnWeHuN2w', 'channel_name': 'Acharya Prashant'},
    {'channel_id': 'UCihUiDJzjyo2ov_qGtW33lw', 'channel_name': 'The Yoga Institute'},
    {'channel_id': 'UCRtAu8OVYVfuNZmTV-Ug0zA', 'channel_name': 'Buddhism'},
    {'channel_id': 'UCrX8UBoue01aj4s0aHmgeQg', 'channel_name': 'DandapaniLLC'},
    {'channel_id': 'UCj9fPezLH1HUh7mSo-tB1Mg', 'channel_name': 'Eckhart Tolle'},
    {'channel_id': 'UCz22l7kbce-uFJAoaZqxD1A', 'channel_name': 'Gaur Gopal Das'},
    {'channel_id': 'UC4qz5w2M-Xmju7WC9ynqRtw', 'channel_name': 'Gurudev Sri Sri Ravi Shanka'},
    {'channel_id': 'UC88A5W9XyWx7WSwthd5ykhw', 'channel_name': 'J. Krishnamurti - Official Channel'},
    {'channel_id': 'UCpw2gh99XM6Mwsbksv0feEg', 'channel_name': 'Moojiji'},
    {'channel_id': 'UCS0s6BFzIcvC2gTH52_vBEA', 'channel_name': 'OSHO International'},
    {'channel_id': 'UCRRtZjnxd5N6Vvq-jU9uoOw', 'channel_name': 'Shi Heng Yi Online'},
    {'channel_id': 'UCclfz6zVWWOpsQsg3OheI3g', 'channel_name': 'Swami Mukundananda'},
    {'channel_id': 'UCZOKv_xnTzyLD9RJmbBUV9Q', 'channel_name': 'Vedanta Society of New York'},
    {'channel_id': 'UC1KIUp4PNCyIwCPTq1hYzWQ', 'channel_name': 'Teal Swan'},
    {'channel_id': 'UCaEtAfisWDXL3eG8u_M2brA', 'channel_name': 'Sandeepmaheshwarispirituality'},
    {'channel_id': 'UCv-oUk8x6SGHMOLrCMDNrsw', 'channel_name': 'MingyurRinpoche'},
    {'channel_id': 'UCQdyCrZpGq4Bbu6V8LPUDWg', 'channel_name': 'bkshivani'},
    {'channel_id': 'UCfwa_zKl8-zC9rQDWIEixgg', 'channel_name': 'Iamjayakishori'},
    {'channel_id': 'UCEk1jBxAl6fe-_G37G7huQA', 'channel_name': 'Bhajan Marg'},
    {'channel_id': 'UCfZF2mRSK5d7WfI9c7BOluQ', 'channel_name': 'Bhavesh'},
    {'channel_id': 'UCKjFQcRLQcwfGWbFKQljouA', 'channel_name': 'Cyber Zeel'},
    {'channel_id': 'UC2S0KiGusFDXWcxwEorulsA', 'channel_name': 'be_a_bassi'},
    {'channel_id': 'UCeP5_FL11TnvXuvrFvALJyA', 'channel_name': 'Gaurav Kapoor'},
    {'channel_id': 'UC-aVkxFEKJYV33-dhFGHxhw', 'channel_name': 'Manik Mahna'},
    {'channel_id': 'UCOu4kfKyeuZ5IibuVByvhgQ', 'channel_name': 'Sapan Verma'},
    {'channel_id': 'UCyGR5vfdIzNj6VRY13nzO-g', 'channel_name': 'Ravi Gupta'},
    {'channel_id': 'UCWdEI-adtq0qZIHCus4-6dQ', 'channel_name': 'Pranav Sharma'},
    {'channel_id': 'UCaUr7y4F9lWGnZ0cbUZyzYA', 'channel_name': 'Aashish Solanki'},
    {'channel_id': 'UCGmhWgV9bmslB0Levatl6qA', 'channel_name': 'Harsh gujral'},
    {'channel_id': 'UCAov2BBv1ZJav0c_yHEciAw', 'channel_name': 'Samay Raina'},
    {'channel_id': 'UCAYum5hCyfkSH5T3vSD_kwQ', 'channel_name': 'Aakash Gupta'},
    {'channel_id': 'UC4muYPMCSYigqIwRjVWkQ2Q', 'channel_name': 'Abhishek Upmanyu'},
    {'channel_id': 'UCIPnPp27nvOVQmbmuz1ioyg', 'channel_name': 'Devesh Dixit'},
    {'channel_id': 'UCNqA44cRILQDwm9MG0vV-Og', 'channel_name': 'Rahul Dua'},
    {'channel_id': 'UCkv2ml-PB1ZKPGfR7XowRSA', 'channel_name': 'Gaurav Gupta'},
    {'channel_id': 'UCj07bxakzjSNSM0GRk_7KOA', 'channel_name': 'Sundeep Sharma'},
    {'channel_id': 'UCQDLUu_qgkVUPDZsfQPxLNQ', 'channel_name': 'Shreeja Chaturvedi'},
    {'channel_id': 'UCo10yRzepDzIt7B7w2wnM1Q', 'channel_name': 'Prashasti Singh'},
    {'channel_id': 'UCxMDGaw3tMLHdH-ZUU4173A', 'channel_name': 'Rajat chauhan'},
    {'channel_id': 'UC4aTcVTewbHtLeV8eK3enwA', 'channel_name': 'Munawar Faruqui'},
    {'channel_id': 'UCmQCEVKEYpKxG8NwXnfIbCw', 'channel_name': 'Jaspreet Singh'},
    {'channel_id': 'UCdiBqa9NjJD7z0uuto-PFJQ', 'channel_name': 'Mohit Morani'},
    {'channel_id': 'UCvLcuNVAb5sKRu7sHuFT0vQ', 'channel_name': 'Vipul Goyal'},
    {'channel_id': 'UCQTmZczX5kGRgaPIgpy6CyQ', 'channel_name': 'max amini'},
    {'channel_id': 'UC8bTQzxgvKkXDAaWkeuUlkg', 'channel_name': 'Trevor Noah'},
    {'channel_id': 'UC2mKA8JTOCeodl9bEK7w42Q', 'channel_name': 'Matt Rife'},
    {'channel_id': 'UCLZc32yrTEMxH1ZO-6fKOzA', 'channel_name': 'The Andrew Schulz'},
    {'channel_id': 'UC2bBsPXFWZWiBmkRiNlz8vg', 'channel_name': 'Abhijit Chavda'},
    {'channel_id': 'UCA295QVkf9O1RQ8_-s3FVXg', 'channel_name': 'Aevy TV'},
    {'channel_id': 'UCPxMZIFE856tbTfdkdjzTSQ', 'channel_name': 'BeerBiceps'},
    {'channel_id': 'UCneyi-aYq4VIBYIAQgWmk_w', 'channel_name': 'Ranveer Allahbadia'},
    {'channel_id': 'UCnC8SAZzQiBGYVSKZ_S3y4Q', 'channel_name': 'Nikhil Kamath'},
    {'channel_id': 'UCRv4waLxgUN0Z-yb2I1Fq4A', 'channel_name': 'Nikhil Kamath Clips'},
    {'channel_id': 'UCzwCEE_PchiBULMnAJqhGVg', 'channel_name': 'Raj Shamani'},
    {'channel_id': 'UCshPyRiu9XTQb2gEagNt-3A', 'channel_name': 'Raj Shamani Clips'},
    {'channel_id': 'UCBqFKDipsnzvJdt6UT0lMIg', 'channel_name': 'Sandeep Maheshwari'},
    {'channel_id': 'UCbT_7qRIrw8TMH8ovjTYBJQ', 'channel_name': 'TRS Clips'},
    {'channel_id': 'UCHOKvQW2N4kLVhKYn2bvF7A', 'channel_name': 'Prakhar ke Pravachan'},
    {'channel_id': 'UCOtQWL2z-tFbI-mgy_Rpdgg', 'channel_name': 'UNFILTERED by Samdish'},
    {'channel_id': 'UChbHERlcXmj4vtQOashiXoQ', 'channel_name': 'Divas Gupta'},
    {'channel_id': 'UCsSZyyGKf9FdpqDmynjVBcA', 'channel_name': 'RealHitVideos'},
    {'channel_id': 'UCpeRzRS1b1NvY4og1huE7jw', 'channel_name': 'dostcast'},
    {'channel_id': 'UCcdCMzwxpy5XmslZQCfujwQ', 'channel_name': 'VarunThakurOfficial'},
    {'channel_id': 'UCtFQDgA8J8_iiwc5-KoAQlg', 'channel_name': 'ANI News'}
]

def get_channel_list():
    """Fetch the list of channel IDs and names."""
    return CHANNELS
