#!/bin/bash

# Colors
CYAN='\033[0;36m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
PURPLE='\033[0;35m'
NC='\033[0m'

echo -e "${PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}        NETRUNNER WORKSPACE CLEANUP UTILITY${NC}"
echo -e "${PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

cd ~/Tools/netrunner-toolkit

# Count workspaces
TOTAL=$(ls -d ejpt_workspace_* 2>/dev/null | wc -l)

if [ $TOTAL -eq 0 ]; then
    echo -e "${YELLOW}[!]${NC} No workspaces found."
    exit 0
fi

# Calculate total size
TOTAL_SIZE=$(du -sh ejpt_workspace_* 2>/dev/null | awk '{sum+=$1} END {print sum}')

echo -e "${CYAN}[FOUND]${NC} $TOTAL workspace(s)"
echo -e "${CYAN}[STORAGE]${NC} Using approximately ${YELLOW}${TOTAL_SIZE}K${NC}"
echo ""

# Show options
echo -e "Cleanup options:"
echo -e "  ${GREEN}1${NC} - Keep last 5, delete rest"
echo -e "  ${GREEN}2${NC} - Keep last 10, delete rest"
echo -e "  ${GREEN}3${NC} - Keep last 3, delete rest"
echo -e "  ${GREEN}4${NC} - List all (no deletion)"
echo -e "  ${GREEN}5${NC} - Archive old workspaces (tar.gz)"
echo -e "  ${RED}6${NC} - Delete ALL workspaces (DANGEROUS!)"
echo -e "  ${YELLOW}0${NC} - Cancel"
echo ""

read -p "Choose option [0-6]: " OPTION

case $OPTION in
    1) KEEP=5 ;;
    2) KEEP=10 ;;
    3) KEEP=3 ;;
    4)
        echo ""
        echo -e "${CYAN}[WORKSPACES]${NC}"
        ls -lhdt ejpt_workspace_* | awk '{print "  " $9, "-", $5}'
        exit 0
        ;;
    5)
        # Archive option
        ARCHIVE_NAME="ejpt_workspaces_archive_$(date +%Y%m%d_%H%M%S).tar.gz"
        echo -e "${CYAN}[ARCHIVING]${NC} Creating $ARCHIVE_NAME..."
        tar -czf $ARCHIVE_NAME ejpt_workspace_*
        echo -e "${GREEN}[SUCCESS]${NC} Archive created: $ARCHIVE_NAME"

        read -p "Delete original workspaces after archiving? (y/N): " DELETE_ORIG
        if [ "$DELETE_ORIG" = "y" ]; then
            rm -rf ejpt_workspace_*
            echo -e "${GREEN}[DELETED]${NC} All workspaces removed (archived)"
        fi
        exit 0
        ;;
    6)
        echo ""
        echo -e "${RED}[WARNING]${NC} About to delete ${RED}ALL $TOTAL${NC} workspaces!"
        read -p "Type 'DELETE ALL' to confirm: " CONFIRM

        if [ "$CONFIRM" = "DELETE ALL" ]; then
            rm -rf ejpt_workspace_*
            echo -e "${GREEN}[SUCCESS]${NC} All workspaces deleted"
        else
            echo -e "${YELLOW}[CANCELLED]${NC} Operation aborted"
        fi
        exit 0
        ;;
    0)
        echo -e "${YELLOW}[CANCELLED]${NC} Operation cancelled"
        exit 0
        ;;
    *)
        echo -e "${RED}[ERROR]${NC} Invalid option"
        exit 1
        ;;
esac

# Keep/Delete logic
if [ $TOTAL -le $KEEP ]; then
    echo -e "${GREEN}[OK]${NC} Only $TOTAL workspace(s) found. Nothing to delete (keeping $KEEP)."
    exit 0
fi

TO_DELETE=$((TOTAL - KEEP))

echo ""
echo -e "${GREEN}[KEEPING]${NC} Most recent $KEEP workspace(s)"
ls -td ejpt_workspace_* | head -$KEEP | while read ws; do
    SIZE=$(du -sh "$ws" 2>/dev/null | awk '{print $1}')
    echo -e "  ${GREEN}→${NC} $ws ($SIZE)"
done

echo ""
echo -e "${YELLOW}[DELETING]${NC} $TO_DELETE old workspace(s)"
ls -td ejpt_workspace_* | tail -$TO_DELETE | while read ws; do
    SIZE=$(du -sh "$ws" 2>/dev/null | awk '{print $1}')
    echo -e "  ${RED}→${NC} $ws ($SIZE)"
done

echo ""
read -p "Proceed with deletion? (y/N): " CONFIRM

if [ "$CONFIRM" = "y" ] || [ "$CONFIRM" = "Y" ]; then
    ls -td ejpt_workspace_* | tail -$TO_DELETE | while read ws; do
        rm -rf "$ws"
        echo -e "${RED}[DELETED]${NC} $ws"
    done

    echo ""
    echo -e "${GREEN}[SUCCESS]${NC} Cleanup complete"

    NEW_TOTAL=$(ls -d ejpt_workspace_* 2>/dev/null | wc -l)
    NEW_SIZE=$(du -sh ejpt_workspace_* 2>/dev/null | awk '{sum+=$1} END {print sum}')
    echo -e "${CYAN}[REMAINING]${NC} $NEW_TOTAL workspace(s) (${NEW_SIZE}K)"
else
    echo -e "${YELLOW}[CANCELLED]${NC} Cleanup aborted"
fi

echo ""
echo -e "${PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
