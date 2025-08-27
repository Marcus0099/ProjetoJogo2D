from code.Const import WIN_HEIGHT
from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.top > WIN_HEIGHT:
                ent.health = 0

    @staticmethod
    def __verify_player_enemy_collision(entity_list: list[Entity]):
        players = [ent for ent in entity_list if isinstance(ent, Player)]
        enemies = [ent for ent in entity_list if isinstance(ent, Enemy)]

        for player in players:
            for enemy in enemies:
                if player.rect.colliderect(enemy.rect):
                    return True
        return False

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for ent in entity_list:
            EntityMediator.__verify_collision_window(ent)
        return EntityMediator.__verify_player_enemy_collision(entity_list)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list[:]:
            if ent.health <= 0:
                entity_list.remove(ent)
