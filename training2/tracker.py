from datetime import datetime, timedelta
from copy import deepcopy
from random import randint
import json
import os
import shutil

class tracker:
    def __init__(self):
        self.locations = None

    def writeToFile(self, file, data):
        with open(file, "a") as log:
            log.write(f"{data['cls']} {str(data['xywh']).replace("[", "").replace("]", "").replace(",", "")} {data['id']}\n")
            # log.write(f"{data['cls']} {data['xywh']}\n")


    def track(self, results):
        # res = []
        # for r in results:
        #     if "id" in r:
        #         res.append(r['id'])
        # print(res)


        if self.locations is None:
            if os.path.exists("results"):
                # If the directory exists, delete it
                shutil.rmtree("results")
                os.makedirs("results")
            else:
                # If the directory doesn't exist, create it
                os.makedirs("results")
            self.locations = []
            # for i in results:
            #     self.locations.append({
            #         'id': i['id'],
            #         'yoloIDs': [i['id']],
            #         'class': i['cls'],
            #         'steps': [{
            #             'time': datetime.utcnow(),
            #             'x': i['xywh'][0],
            #             'y': i['xywh'][1],
            #             'w': i['xywh'][2],
            #             'h': i['xywh'][3]
            #         }]
            #     })
            for i in results:
                self.locations.append({
                    'id': i['id'],
                    'yoloIDs': [i['id']],
                    'class': i['cls'],
                    'steps': [{
                        'time': datetime.utcnow(),
                        'x': i['xywh'][0],
                        'y': i['xywh'][1],
                        'w': i['xywh'][2],
                        'h': i['xywh'][3]
                    }]
                })

            self.writeToFile(f"results/{i['filename']}", i)

        else:
            for o in results:
            # if result id matches a location id - add a step to existing location id
                match = next((loc for loc in self.locations if loc['yoloIDs'][-1] == o['id']), None)
                if match:
                    # print('we matched id: ' + str(match['id']))
                    match['steps'].append({
                        'time': datetime.utcnow(),
                        'x': o['xywh'][0],
                        'y': o['xywh'][1],
                        'w': o['xywh'][2],
                        'h': o['xywh'][3]
                    })
                else:
                    # if the result is near an existing location which doesn't appear in these results - replace the
                    # location id with the result id
                    for loc in self.locations:
                        if (abs(o['xywh'][0] - loc['steps'][-1]['x']) < 100 and
                                abs(o['xywh'][1] - loc['steps'][-1]['y']) < 100 and
                                not any(result['id'] == loc['yoloIDs'][-1] for result in results)):
                            # print('we swapped an id: ' + str(loc['id']) + ' with: ' + str(o['id']))
                            loc['yoloIDs'].append(o['id'])
                            loc['steps'].append({
                                'time': datetime.utcnow(),
                                'x': o['xywh'][0],
                                'y': o['xywh'][1],
                                'w': o['xywh'][2],
                                'h': o['xywh'][3]
                            })
                            break

                # if we still haven't added the current result id into the locations, add a new location id
                if not any(loc['yoloIDs'][-1] == o['id'] for loc in self.locations):
                    # print('we added a new id: ' + str(o['id']))
                    self.locations.append({
                        'id': o['id'],
                        'yoloIDs': [o['id']],
                        'class': o['cls'],
                        'steps': [{
                            'time': datetime.utcnow(),
                            'x': o['xywh'][0],
                            'y': o['xywh'][1],
                            'w': o['xywh'][2],
                            'h': o['xywh'][3]
                        }]
                    })
                self.writeToFile(f"results/{o['filename']}", o)
                pass
        # self.clearEephemeralLocations()
