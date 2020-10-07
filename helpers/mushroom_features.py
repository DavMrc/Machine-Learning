import json


class MushroomFeatures(object):
	__features = json.load(open('./helpers/mushroom_features.json'))

	@ classmethod
	def valuename_of(cls, feature, letter):
		"""
		Returns the full string name for class `letter` of feature `feature`.
		"""
		for _feature, values in cls.__features.items():
			for name, _letter in values.items():
				if _feature == feature and _letter == letter:
					return name

	@ classmethod
	def values_short(cls, feature):
		"""
		Returns a list of the letters representing all the possible values for `feature`.
		"""
		return cls.__features[feature].values()
