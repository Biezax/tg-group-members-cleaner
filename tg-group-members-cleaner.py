from telethon import TelegramClient, types
import asyncio
import argparse

api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
channel_username = 'YOUR_CHANNEL_USERNAME'

async def analyze_deleted_accounts(remove=False):
    async with TelegramClient('session_name', api_id, api_hash) as client:
        channel = await client.get_entity(channel_username)
        
        total_members = 0
        deleted_accounts = 0
        deleted_list = []

        async for participant in client.iter_participants(channel):
            total_members += 1
            
            if participant.deleted:
                deleted_accounts += 1
                deleted_list.append({
                    'id': participant.id,
                    'joined_date': participant.participant.date if hasattr(participant, 'participant') else None
                })
                if remove:
                    try:
                        await client.kick_participant(channel, participant)
                        print(f"Removed account with ID: {participant.id}")
                    except Exception as e:
                        print(f"Error removing {participant.id}: {str(e)}")

        print(f"\nStatistics for channel {channel.title}")
        print(f"Total members: {total_members}")
        print(f"Deleted accounts: {deleted_accounts}")
        print(f"Percentage of deleted: {(deleted_accounts / total_members * 100):.2f}%")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--rm', action='store_true', help='Remove deleted accounts')
    args = parser.parse_args()
    
    asyncio.run(analyze_deleted_accounts(args.rm))
